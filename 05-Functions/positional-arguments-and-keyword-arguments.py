# Positional arguments has to do with entering the argument in the right place as its parameter previously decided

# Keyword arguments has to do with entering the argument as an assignment value to the parameter in the function call.

# Positional argument
def  addStuff(a, b):
    print(a + b)


addStuff(2, 4)
# 2 is marked for a while 4 is marked for b

def subtractStuff(y, w):
    print(y - w)

subtractStuff(y=4, w=3)
# Keyword argument here