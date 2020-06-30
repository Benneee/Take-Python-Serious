# Class attributes are attributes accessible within a class
# This can be used to store a variable that is not directly related to the state of any object created from that class

class Counter():
    count = 0
    # say we want to keep track of how many objects is created from this class
    def __init__(self):
        Counter.count += 1
    # Whenever this init method runs, we are going to know how many times an object has been created 

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of objects created: {cls.count}")
        return two_counters

print(Counter.count)
c1 = Counter()
print(Counter.count)

# 1.
print(c1.count)

c2, c3 = Counter.create_two()
print(Counter.count)


# 3.
print(c2.count)
# Class attributes can be accessed within the instances of that class
# However, it will only give us the value of the current state of that variable