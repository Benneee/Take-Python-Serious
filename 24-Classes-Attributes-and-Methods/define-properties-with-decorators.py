class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

# We want the dollars method to be a property, not an instance method,
# So we use the inbuilt decorator for property to mark the dollars method
    @property
    def dollars(self):
        return self._cents / 100

# To create the setter property, we use the property decorator as well, with a difference this time
# The property we are concerned with here is dollars, hence we call its setter property / method
# The method name has to be the same property marked as the getter method
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100
# Example
bank_account = Currency(5000)
print(bank_account.dollars)

bank_account.dollars = 10000
print(bank_account.dollars)

# This will not run because we have a validator checking the value of the dollars amount
bank_account.dollars = -10000
print(bank_account.dollars)