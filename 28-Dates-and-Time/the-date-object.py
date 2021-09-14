# Date and Time objects are immutable
from datetime import date

# The date constructor object accepts 3 mandatory arguments
# - the year
# - the month
# - the day

birthday = date(1992, 9, 7)
# print(birthday)

# To get today's date, a class method exists on the date class
today = date.today()
# print(today)

# print(birthday.day)
# print(birthday.month)
# print(birthday.year)

weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

weekday_of_birth = birthday.weekday()
print(weekdays[weekday_of_birth])