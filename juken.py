from time import sleep
import schedule
from datetime import datetime

dt = datetime(2020, 10, 1)


def job():
    nokori = dt - now
    day = nokori.days
    days = int(day) + 1
    print(f'本番まで{days}日だZO!!')


schedule.every().day.at('00:00').do(job)


while True:
    now = datetime.now()
    schedule.run_pending()
    sleep(1)
