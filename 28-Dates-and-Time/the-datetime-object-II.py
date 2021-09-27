# string from time method returns the string representation of the date object in whatever format we need
# By format, we mean the order and representation of the elements, either of the date items can be repositioned
# separators can be modified as well

from datetime import datetime

today = datetime.today()

# Whatever is passed into the method is very important for python's interpretation
print(today.strftime("%m")) # Month in number: e.g 09
print(today.strftime("%m %d")) # Month and day in number separated by space
print(today.strftime("%m/%d/%Y")) # Full date in number separated by slashes

print(today.strftime("%A")) # Day of the week: e.g Thursday
print(today.strftime("%B")) # Month in text: e.g September