from fastapi.routing import APIRouter
from configs.schedulerConfig import get_jobs, add_job
from schemas.schedulerSchemas import SchedulerTaskBaseSchema

app = APIRouter(prefix="/cron", tags=["Scheduler"])


@app.get("/", response_model=list[SchedulerTaskBaseSchema])
async def list_jobs():
    """returns a list of the jobs in the scheduler"""
    result = await get_jobs()
    return result


@app.get("/mock")
async def list_jobs_mock():
    """returns a list of the jobs in the scheduler"""
    return [{"id": "some id string", "name": "task name"}]


@app.post("/")
async def list_jobs():
    """returns a list of the jobs in the scheduler"""
    await add_job()
