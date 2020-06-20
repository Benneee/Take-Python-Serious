# Object-oriented programming is a paradigm for code organization and design that views a software
# ..program as a collection of objects that interacts with each other

# OBJECTS
# An object is a container of data (attributes) and behavior (methods)

# Attributes define an object's state or internal data. They can be viewed as variables belonging to an object
# A method is a command or an instruction to send to an object. It is actually a function within the class

# Example: a football
# Attributes
# 1. Manufacturer: 'reebok' -> string
# 2. Weight: 5.6 -> float
# 3. Color: ['yellow', 'blue'] -> list

# Methods
# 1. Kick (Doesn't add any physical attribute to the ball, but changes its position)
# 2. Inflate (Alters the weight attrubute)
# 3. Paint (Can add a color to the list of colors in the attributes of the football)

# Summarily, methods are things we can do to an object to alter its physical state, they don't have to but they can


# CLASSES
# A class is a blueprint for creating a new object.
# A class definition describes the attributes and methods that each object made from the class will have
# The class name must always represent a single resource

# INSTANCES
# An instance is an object created from a class. The act of creating one is called "instantiation"
# Objects created from the same class are independent of each other.

class Person():
  pass


class DatabaseConnection():
  pass


# Creating an instance of the Person class
benneee = Person()
teenah = Person()

# Creating an instance of the DatabaseConnection class
dc = DatabaseConnection()

print(benneee)
print(teenah)

print(dc)
