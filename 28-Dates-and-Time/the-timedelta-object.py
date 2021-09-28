from datetime import datetime, timedelta

# Basic way to get time difference
birthday = datetime(1992, 9, 7)
today = datetime.now()

diff = today - birthday
print(diff)
print(type(diff))

# The diff variable is a timedelta object
# So we can use methods under the timedelta object for other purposes
print(diff.total_seconds())

