import datetime as dt
import time

monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    time.sleep(1)
    seconds = 0
    days = 0
    for i in range(1900, int(str(dt.date.today())[:4])):
        if i % 100 == 0 and i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
              seconds = seconds + 31622400
        else:
            seconds = seconds + 31536000

    for i in range(int(str(dt.date.today())[5:7]) - 1):
        if str(dt.date.today())[5:7] == "02":
            year = str(dt.date.today())[:4]
            if year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                days = days + 29
            else:
                days = days + 28
        else:
            days = days + monthdays[i]

    for i in range(days - 1):
        seconds = seconds + 86400

    for i in range(int(str(dt.date.today())[8:10])):
        seconds = seconds + 86400

    for i in range(int(str(dt.datetime.now())[11:13]) - 1):
        seconds = seconds + 3600

    for i in range(int(str(dt.datetime.now())[14:16])):
        seconds = seconds + 60
    seconds = seconds + int(str(dt.datetime.now())[17:19])
    print(seconds)
