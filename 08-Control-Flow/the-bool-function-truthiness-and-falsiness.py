# Values that are truthy have their boolean equivalent to be True
# Values that are falsy have their boolean equivalent to be False

# Truthiness or Falsiness aren't exactly True or False, they only tell you whether a number, string or object 
# ...evaluates to the concept of being True or False.

# For Numbers
# 0 is a falsy value, however, any other number is truthy, negatives are also falsy
if 0:
    print("I won't print")

if 1:
    print("I will always print because I am truthy")


# For Strings
# An empty string(just quotes) is a falsy value but any other string is falsy
if "":
    print("I won't print because I am falsy")

if "hello":
    print("I am truthy bro")


# A way to know if a value is truthy or falsy is to pass it through the bool method

print(bool(0))
print(bool(2))
print(bool("how far"))
print(bool(""))

def checkBoolValue(num: int):
    if bool(num) == True:
        print("Oshey! Truthy of life!!")


checkBoolValue(3)

def even_or_odd(num):
    if num % 2 == 0:
        print("even")
    if num % 2 == 1:
        print("odd")


even_or_odd(19)
even_or_odd(0)
even_or_odd(101)