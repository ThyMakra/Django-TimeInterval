from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastApi

# runtime-initialization
# this is being called from weather/apps.py > WeatherConfig.ready()
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastApi.update_forecast, 'interval', seconds=2)
    scheduler.start()