from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .sensor_logic import generate_all_data

scheduler = BackgroundScheduler()

def start_scheduler_job():
    scheduler.add_job(generate_all_data, 'interval', seconds=10, next_run_time=datetime.now())
    scheduler.start()