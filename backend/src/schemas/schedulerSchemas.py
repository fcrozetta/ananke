from pydantic import BaseModel, ConfigDict
import datetime as dt


class SchedulerIntervalTriggerBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    trigger_type: str = "interval"
    interval_length: float
    start_date: dt.datetime


class SchedulerDateTriggerBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    trigger_type: str = "date"
    run_date: dt.datetime


class SchedulerCronTriggerBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    trigger_type: str = "cron"
    run_date: dt.datetime


class SchedulerTaskBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    next_run_time: dt.datetime
    pending: bool
    trigger: SchedulerIntervalTriggerBaseSchema | SchedulerDateTriggerBaseSchema
