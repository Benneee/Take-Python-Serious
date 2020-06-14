# Equality tests whether two objects are equal, whether they have the same value, shape or structure

# Identity checks if two names in the program point to the same object in the computer memory.
# We can check for object identity with the "is" keyword and it is more stricter than the "==" for equality

# For immutable objects, python doesn't need to create separate objects to be referenced by variables pointing to the same data. This is however not the case for mutable objects

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c) # Of course, they will be equal because they contain the same object content (TRUE)

print(a is c) # False, because Python creates another object in memory for c. This is largely because the object type is mutable 