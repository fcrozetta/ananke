from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.spiderRouter import app as spider

app = FastAPI(
    title="Fer's automated routines",
    description="You should use this with a frontend.Check port 80 http://localhost/",
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "hello world"


app.include_router(spider)
