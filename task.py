from celery import Celery
from celery.schedules import crontab
from config.literal import locations
from tasks.import_location import import_location
from tasks.import_forecasts import ImportForecasts

app = Celery('task', broker="amqp://localhost")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        import_locations_forecasts_task_cron.s(),
    )

@app.task
def import_locations_forecasts_task_cron():
    import_location_task.delay()
    for location in locations:
        import_locations_forecasts.delay(location)

@app.task
def import_location_task():
    import_location()
    return {'Success': True}

@app.task
def import_locations_forecasts(city: str):
    import_forecasts = ImportForecasts()
    import_forecasts.import_forecasts(city)
    return {'Success':city}
        