employee = ("Bob", "Johnson", "Manager", 50)

# Unpacking with * works like how we use the rest operator
# If we assign the first two variables to two different variables and the other two to a single variable
# We use the * on the variable name we want to hold the remaining values of the tuple

first_name, last_name, *details = employee

# The details variable will be a list and not a tuple

# print(details)

# Reversing this would have Python allocating the last two elements in the tuple to the last two
*names, position, age = employee
# print(names)