# Getters and setters are instance methods that get / set attribute values on an object
# getter = reader, setter = writer / overwriter

class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    # A reader method
    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

# Notice that we did not explicitly set a feet attribute
    # This property now becomes what is accessed when we create an object
    feet = property(_get_feet, _set_feet)


h = Height(5)
# This is not an attribute but a property
print(h.feet)

# This code above runs like this:
# Line 17 is called and the very first method in the arguments is fired
# This fired method is the get method, it calls line 9, which then takes the value from line 5
# and does its conversion, then returns to us the value we need.

# When we try to set a value for feet by assigning h.feet to a value, the set method within the property method is called
h.feet = 6
print(h.feet)

# At this point, we run code on line 12.

# Summary: Properties gives the appearance of attributes, but in the background, they will invoke methods for you.
# Either a getter method or a setter method.
# This helps us to afford validation in the setter method, for example.
# Note that there will be a recursion problem if the property name and the attribute name for the class are the same.
# e.g inches