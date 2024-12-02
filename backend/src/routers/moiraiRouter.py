from fastapi.routing import APIRouter
from fastapi.websockets import WebSocketDisconnect, WebSocket
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
        await websocket.send_text(event)

    await websocket.accept()
    await e.add_listener(job_id, listener=listener)
    try:
        while True:
            event = await websocket.receive_text()
            # await websocket.send_text(
            #     event
            # )  # Echo the received message back to the client
    except WebSocketDisconnect:
        await e.remove_listener(job_id, listener=listener)
