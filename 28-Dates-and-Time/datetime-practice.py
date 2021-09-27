from datetime import datetime, date, time

today = datetime(2000, 11, 17, 6, 0, 0)
friday = today.strftime('%a')
print(friday)

fulldate = today.strftime("%B %d, %Y")
print(fulldate)

day_of_year = today.strftime("%j")
print(day_of_year)

week_of_year = today.strftime("%W")
print(week_of_year)

time_of_day = today.strftime("%H:%M:%S %p")
print(time_of_day)

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)

def one_from_two(date_object, time_object):
    return datetime.combine(date_object, time_object)


print(one_from_two(some_date, some_time))
