# For mutable objects, when the variable is reassigned, it shares the same data with the original variable
# So if the data is altered, even the data being held by the reassigned variable is altered
# Because both variables are actually holding the same data in memory
a = [1, 2, 3]
b = a

a.pop()

# print(a, b)

# The case for immutable types is actually different, because the initial value isn't affected when the variable is reassigned
a = 3
b = a

a = 5

print(a, b)
# b still holds the initial value of a as its value, the variable is only connected to the data in this sense
# In the other example above, both variables are connected because they hold the same data in memory