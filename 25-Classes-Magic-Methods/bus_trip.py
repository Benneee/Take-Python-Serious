# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.
class BusTrip():
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price

# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.
    def __str__(self):
        return f"You paid {self.price} to {self.company} to go to {self.destination}."

# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.
    @staticmethod
    def check_difference(value1, value2):
        difference = abs(value1 - value2) <=3
        return difference

    def __eq__(self, other_trip):
        if self.destination == other_trip.destination and self.check_difference(self.price, other_trip.price):
            return True
        else:
            return False
        

# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2) # True - same destination and insignificant price difference
print(boston1 == boston3) # False - large price difference