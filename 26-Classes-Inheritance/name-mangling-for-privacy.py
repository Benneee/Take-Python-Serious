# Name mangling is done by using double underscores for an attribute.

# The python interpreter knows to mangle the attribute or method name once there's a double underscore before it
# Hence, making sure it is not easily accessible

class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print('This is coming from some_method')


class SpecialNonsense(Nonsense):
    pass


n = Nonsense()
sn = SpecialNonsense()


# print(n.__some_attribute) # AttributeError: 'Nonsense' object has no attribute '__some_attribute'
# print(sn.__some_attribute) # AttributeError: 'SpecialNonsense' object has no attribute '__some_attribute'

# n.__some_method() # AttributeError: 'Nonsense' object has no attribute '__some_method'

# However, to get the actual attributes, we need to pull a little trick
n._Nonsense__some_method()
print(n._Nonsense__some_attribute)