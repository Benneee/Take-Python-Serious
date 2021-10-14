# Set up and tear down are used to create test fixtures
# A test fixture is a piece of code that constructs and configures an object or system under test

import unittest

class Address():
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant():
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    @property
    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}"


class TestRestaurant(unittest.TestCase):
    # These execute before and after each test respectively
    # setUp sets up every necessary functionality for a test

    # The method names, setUp and tearDown, need to be written the way they've been written below
    # because they override methods with the same name inherited from the TestCase class
    def setUp(self):
        print('Runs before each test')
        address = Address(city = 'Ogudu', state = 'Lagos')
        owner = Owner(name = 'Jack', age = 60)
        # for variables like the one below, it's best to have it assigned to "self" so it doesn't get lost to memory
        self.golden_palace = Restaurant(address, owner)

    def tearDown(self):
        print('Runs after each test')


    def test_owner_age(self):
        self.assertEqual(self.golden_palace.owner_age, 60)

    def test_summary(self):
        self.assertEqual(
            self.golden_palace.summary,
            'This restaurant is owned by Jack and is located in Ogudu'
        )


if __name__ == '__main__':
    unittest.main()