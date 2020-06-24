# Protected attributes are attributes designated as being internal or semi-private to an object
# They are not meant to be modified directly, rather, their values should only be modified by instance methods

# Encapsulation is one of the principles of OOP. It is the idea that data should be bundled together with methods 
# ... that work on that data

# We show a protected attribute by starting the attribute name with an underscore
# It is a notifier to tell anyone that they should not be manually setting any value to that attribute, but by using a method to modify.
class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

# BY doing the following, we have provided interfaces to ensure the private attributes can be accessed or modified
    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1
    
iphone = SmartPhone()

iphone.update_firmware()
print(iphone.get_os_version())
