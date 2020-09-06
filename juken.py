from time import sleep
from datetime import datetime

dt = datetime(2020, 10, 1)
while True:
    date = datetime.now()
    date_str = str(date)
    tim = date_str[11:-10]
    if '00:00' == tim:
        nokori = dt - date
        day = nokori.days
        days = int(day) + 1
        print(f'本番まで{days}日だZO!!')
        sleep(60)
