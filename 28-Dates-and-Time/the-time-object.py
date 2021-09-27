from datetime import time

# If no arguments are passed, the time object results to midnight time
# The arguments for the time object is:
# Hours
# Minute
# Second
# Microsecond

# These arguments are optional and any one not passed in defaults to 0
# The time object is also a 24-hour clock

noon = time(12)
print(noon)