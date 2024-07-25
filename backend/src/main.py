from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from routers.spiderRouter import app as spider
from routers.schedulerRouter import app as cron

from configs.schedulerConfig import scheduler


app = FastAPI(
    title="Fer's automated routines",
    description="You should use this with a frontend.Check port 80 http://localhost/",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("START")
    scheduler.start()
    yield
    print("STOP")
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "hello world"


app.include_router(spider)
app.include_router(cron)
