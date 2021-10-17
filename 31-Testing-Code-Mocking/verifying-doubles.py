import unittest
from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1


# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

# The spec attribute helps us to recreate the BurritoBowl class, not its instance
class_mock = MagicMock(spec = BurritoBowl)
# If we attempt to call an attribute or method that doesn't exist in the class specified, Python will raise an exception
print(class_mock.restaurant_name)
print(class_mock.steak_special())

# To mock the instance/object instead of the class
instance_mock = MagicMock(spec = BurritoBowl.steak_special())
# The spec_set parameter is a stricter version of the spec parameter that does not allow a new attribute to be set on the class
# instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock.protein)
print(instance_mock.rice)
print(instance_mock.guacamole_portions)


instance_mock.beans = True # This line will not throw an error
print(instance_mock.beans)

if __name__ == '__main__':
    unittest.main()