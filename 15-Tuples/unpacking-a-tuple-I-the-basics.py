# A tuple object can be unpacked, this means that we can assign its ordered elements to variables within our program
employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, position, age = employee; # Unpacking
# This same thing works with Lists

print(first_name);

a = 5
b = 10

# Using tuple unpacking to swap variable values
# It should be noted that what happens on the RHS occurs first, also, the presence of a comma makes something a tuple
# The values ar bundled as a tuple and unpacked to the variables on the LHS
b, a = a, b
print(a, b)