import asyncio
from fastapi.routing import APIRouter
from fastapi.websockets import WebSocketDisconnect, WebSocket, WebSocketState
from services.scrapy import Spider
from moirai_engine.core.engine import Engine
from moirai_engine.utils.samples import hello_world, slow_hello_world

app = APIRouter(prefix="/moirai", tags=["Moirai"])


async def listener(event):
    print(event)


e = Engine(listener=listener)


@app.get("/hello")
async def add_hello():
    await e.start()
    job = slow_hello_world()
    await e.add_job(job, listener)
    return {"job_id": job.id}


@app.websocket("/{job_id}")
async def notifications(websocket: WebSocket, job_id: str):
    async def listener(event):
        if websocket.client_state == WebSocketState.DISCONNECTED:
            # await e.remove_listener(job_id, listener=listener)
            return
        await websocket.send_text(event)

    await websocket.accept()
    e.add_listener(listener=listener, job_id=job_id)
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        ...
        # await e.remove_listener(job_id, listener=listener)
