import apscheduler
import apscheduler.job
import apscheduler.schedulers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
import apscheduler.schedulers.base

from tasks.helloWorldTask import HelloWorldTask


jobstores = {"default": MemoryJobStore()}

# Initialize an AsyncIOScheduler with the jobstore
scheduler = AsyncIOScheduler(jobstores=jobstores)


async def get_jobs():
    return apscheduler.schedulers.base.BaseScheduler.get_jobs(scheduler)


x = HelloWorldTask()


async def add_job():

    # apscheduler.schedulers.base.BaseScheduler.add_job(
    #     scheduler, x.run, "interval", seconds=5
    # )
    apscheduler.schedulers.base.BaseScheduler.add_job(
        scheduler, x.run, "cron", day_of_week="mon-sun", hour=23, minute=44
    )
    # apscheduler.schedulers.base.BaseScheduler.add_job(
    #     scheduler, x.run, "date", run_date="2024-07-26 14:00:00"
    # )


def job_manual():
    print("hello world")


# # Job running every 10 seconds
# @scheduler.scheduled_job("interval", seconds=10)
# def scheduled_job_1():
#     print("scheduled_job_1")


# # Job running at a specific date and time
# @scheduler.scheduled_job("date", run_date="2024-07-26 11:00:00")
# def scheduled_job_2():
#     print("scheduled_job_2")


# # Job running daily at 23:44:00
# @scheduler.scheduled_job("cron", day_of_week="mon-sun", hour=23, minute=44, second=0)
# def scheduled_job_3():
#     print("scheduled_job_3")
