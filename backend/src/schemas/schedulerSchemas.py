from pydantic import BaseModel, ConfigDict, model_serializer, field_serializer
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
    start_date: dt.datetime | None
    end_date: dt.datetime | None
    crontab: object | None

    @field_serializer("crontab")
    def serialize_crontab(self, crontab: object, _info):
        x = tmp_dict = {k: str(v) for (k, v) in zip}
        return f"{x['minute']} {x['hour']} {x['day']} {x['month']} {x['day_of_week']}"


class SchedulerTaskBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    next_run_time: dt.datetime
    pending: bool
    trigger: (
        # SchedulerIntervalTriggerBaseSchema
        # | SchedulerDateTriggerBaseSchema
        SchedulerCronTriggerBaseSchema
    )
