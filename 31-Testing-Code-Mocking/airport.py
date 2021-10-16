# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 
from unittest.mock import Mock
# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.


# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.

# {
#   "Atlanta": "12:00PM",
#   "Nashville": "04:30PM"
# }

# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.

# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.

# EXAMPLE
#
# Given an airport Mock...
#
# print(airport.gates)      # ["A1", "B2", "C3"]
# print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
# print(airport.close())    # Closing
# print(airport.open())     # Opening...
# print(airport.open())     # Already open

airport = Mock(
    gates = ["A1", "B2", "C3"],
    departures =  {
    "Atlanta": "12:00PM",
    "Nashville": "04:30PM"
    }
)
airport.close.return_value = "Closing"
airport.open.side_effect = ['Opening...', 'Already open']

print('departures', airport.departures)
print('gates', airport.gates)
print('close', airport.close())
print('open', airport.open())
print('open', airport.open())