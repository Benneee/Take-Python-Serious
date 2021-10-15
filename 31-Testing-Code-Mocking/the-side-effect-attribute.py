# The side-effect attribute allows us set a custom implementation for the mock object's return value
# when the mock method is invoked

from unittest.mock import Mock
from random import randint


def generate_number():
    return randint(1, 10)


# call_me_maybe = Mock()
# call_me_maybe.side_effect = generate_number

# print(call_me_maybe())

# The side_effect attribute helps us get dynamic return values and can be used 
# in place of "return_value" attribute when different values are needed


call_me_maybe = Mock(
    side_effect = generate_number
)

print(call_me_maybe())