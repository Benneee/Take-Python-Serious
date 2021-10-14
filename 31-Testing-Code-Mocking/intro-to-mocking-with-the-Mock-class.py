# A mock is an object that takes the place of another object in a test
from unittest.mock import Mock

pizza = Mock()

# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ['Pepperoni', 'Mushroom', 'Sausage']

# If we try to access a property or method that hasn't been declared in the instantiation of the Mock object
# we get a new Mock object.


# a configure_mock method helps to create mock objects by accepting a number of arguments
# each keyword parameter stands as the attribute for the object and the argument provided serves as the value

pizza.configure_mock(
    size = 'Large',
    price = 19.99,
    toppings = ['Pepperoni', 'Mushroom', 'Sausage']
)


print(pizza.size)
print(pizza.toppings)
print(pizza.price)
print(pizza.anything)
print(pizza.cover_with_cheese())