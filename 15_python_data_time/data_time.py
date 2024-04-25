""" Python has got datetime module to handle date and time"""
import datetime
from datetime import datetime, date, time, timedelta

# print(dir(datetime)) # With dir or help built-in commands it is possible to know the available functions in a certain module

# # Getting date time information 
# now = datetime.now()
# print(now)
# day = now.day
# month = now.month
# year = now.year
# hour = now.hour 
# minute = now.minute
# second = now.second
# time_stamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', time_stamp)
# # timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
# print(f'{day}/{month}/{year}, {hour}:{minute}')

# # Formatting Date Output Using strftime
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)

# # String to Time using strptime
# date_string = "25 April, 2024"
# print("date_string = ", date_string)
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)

# # Using date from datetime
# dat = date(2024, 1, 1)
# print(dat)
# print("Current date:", dat.today())
# today = dat.today()
# print("Current year: ", today.year)
# print("Current month: ", today.month)
# print("Current day:", today.day)

# # Time Objects to Represent Time
# a = time()
# print("a = ", a)

# b = time(10, 30, 50)
# print("b = ", b)

# c = time(hour=10, minute=30, second=50)
# print("c =", c)

# d = time(10, 30, 50, 200555)
# print("d =", d)

# # Difference Between Two points in Time using
# today = date(year=2019, month=12, day=5)
# new_year = date(year=2020, month=1, day=1)
# time_left_for_newyear = new_year - today
# # Time left for new year:  27 days, 0:00:00
# print('Time left for new year: ', time_left_for_newyear)

# t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
# t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
# diff = t2 - t1
# print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# # Difference Between two points in Time using timedelata
# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)

print(" ------------------------------- Ejercicios -------------------------------")
# # 1
# today = datetime.today()
# year = today.year
# month = today.month
# day = today.day
# hour = today.hour
# minute = today.minute
# second = today.second
# timestamp = today.timestamp()

# # 2 
# print(today.strftime("%m/%d/%Y, %H:%M:%S"))

# # 3 
# string = "5 December, 2019"
# string_object = datetime.strptime(string, "%d %B, %Y")
# print("Today is", string_object)

# # 4 
# new_year = datetime(year=2025, month=1, day=1, hour=0, minute=0)
# t = datetime.today()
# actual_year = datetime(year = t.year, month=t.month, day=t.day, hour=t.hour, minute=t.minute, second= t.second)
# time_to_new_year = new_year - actual_year
# print("The time to new year is:", time_to_new_year)

# 5 
today = datetime.today()
diff = today - datetime(year=1970, month=1, day=1)
print(diff) 
