import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prodject_obshaga.settings')
django.setup()

from obshaga.scheduler import start_scheduler_job

start_scheduler_job()


import time
while True:
    time.sleep(60)