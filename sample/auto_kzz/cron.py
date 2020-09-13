from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

accounts = ['ht_client_liaolong.json', 'ht_client_chenjun.json']

def job0():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    os.system("python KZZ.py " + accounts[0])

def job1():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    os.system("python KZZ.py " + accounts[1])

# # BlockingScheduler
scheduler = BlockingScheduler()

scheduler.add_job(job0, 'cron', day_of_week='0-6', hour=8, minute=55, misfire_grace_time=43200)
scheduler.add_job(job1, 'cron', day_of_week='0-6', hour=8, minute=57, misfire_grace_time=43200)

scheduler.start()