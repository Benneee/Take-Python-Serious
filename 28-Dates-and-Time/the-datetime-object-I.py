from datetime import datetime

# Only year, month and day arguments are required, other parameters will default to 0
print(datetime(1992, 9, 7))

# There are also two datetime objects that return the current date and time in datetime object style
# today() and now()
print(datetime.now())
today = datetime.today()
print(today)

# Weekday is also represented in integers, with 0 for Monday
print(today.weekday())

# Datetime objects are immutable
# We can however return instances of the date changed in one part with the replace method
same_time_twenty_years_ago = today.replace(year = 1992)
print(same_time_twenty_years_ago)