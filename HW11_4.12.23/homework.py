import pytz
import datetime
#      number1
# date_string = '2015-06-16'
# date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
# week = date.isocalendar()[1]
# print(week)

#      number2
# year = 2015
# week = 50
# firstDay = datetime.datetime.strptime('2015-50-1',"%Y-%W-%w")
# monday = firstDay - datetime.timedelta(firstDay.weekday())
# print(monday)

#      number3
# sundays = [datetime.datetime(2023, 1, 1) + datetime.timedelta(i)
#            for i in range(365) if (datetime.datetime(2023, 1, 1) + datetime.timedelta(i)).weekday() == 6]
#
# for sunday in sundays:
#     print(sunday.strftime('%Y-%m-%d'))

#      number4
# date = datetime.datetime(2023, 12, 18)
# add = 5
# new_date = date + datetime.timedelta(365 * add)
# print(new_date.strftime('%Y-%m-%d'))

#     number5
# time_utc = datetime.datetime.now(datetime.timezone.utc)
# print(f"Время по Гринвичу: {time_utc}")
# time_local = datetime.datetime.now()
# print(f"Время в Астане: {time_local}")

#      number6
# dateOne = datetime.datetime(2023, 4, 15)
# dateTwo = datetime.datetime(2016, 8, 3)
# days = dateOne - dateTwo
# print(days)

#      number7
# dateOne = datetime.timedelta(days=10, hours=15, minutes=48, seconds=34)
# dateTwo = datetime.timedelta(days=18, hours=5, minutes=26, seconds=59)
# difference = dateTwo - dateOne
# print(difference)