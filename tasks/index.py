from celery import Celery
from celery.schedules import crontab
from settings import variables
from config.literal import locations
from tasks.import_location import import_location
from tasks.import_forecasts import ImportForecasts
from tasks.check_database import check_database

celery = Celery('task', broker='amqp://localhost')

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        import_locations_forecasts_task_cron.s(),
    )

@celery.task
def check_task():
    print('Initialized Connection')
    result = check_database()
    if not(result):
        import_locations_forecasts_task_cron.delay()

@celery.task
def import_locations_forecasts_task_cron():
    import_location_task.delay()
    for location in locations:
        import_locations_forecasts.delay(location)

@celery.task
def import_location_task():
    import_location()
    return {'Success': True}

@celery.task
def import_locations_forecasts(city: str):
    import_forecasts = ImportForecasts()
    import_forecasts.import_forecasts(city)
    return {'Success':city}
        
