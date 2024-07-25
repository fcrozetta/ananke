from fastapi.routing import APIRouter
from configs.schedulerConfig import get_jobs, add_job

app = APIRouter(prefix="/cron", tags=["Scheduler"])


@app.get("/")
async def list_jobs():
    """returns a list of the jobs in the scheduler"""
    return str(await get_jobs())


@app.post("/")
async def list_jobs():
    """returns a list of the jobs in the scheduler"""
    await add_job()
