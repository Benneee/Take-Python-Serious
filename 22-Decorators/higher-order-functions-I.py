# A higher order function is a function that either accepts a function as an argument or returns a function as a return value

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# The higher oreder function
def calculateStuff(func, a, b):
    return func(a, b)

print(calculateStuff(add, 10, 22))