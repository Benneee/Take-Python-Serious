# A tuple is a fixed-length unchangeable / immutable list
# A collection of strings that are comma-separated.

foods = "Sushi", "Stake", "Guacamole" 

# Standard Syntax | Best practice
foods = ("Sushi", "Stake", "Guacamole");


# Tuples are created by the presence of a comma, while lists are created with the square brackets
# However, parentheses are need for an empty tuple
mystery = (1,)
print(type(mystery))

singleTuple = tuple(["abc"])
scattered = tuple("abc")

print(scattered == singleTuple) # False
# singleTuple will pack the value abc as a single element for the tuple
# while scattered will be presented as a tuple of three characters because the tuple assumes we want a tuple 
# ... containing all those characters separately
# To create an intact tuple, pass the elements in the way you want it to appear in the tuple as a list to the tuple function