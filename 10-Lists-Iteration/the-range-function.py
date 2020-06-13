# The range function is used to generate a collection of ordered items
# It also produces a generator object and we can iterate over the product with a for loop

for value in range(5):
    print(value) # This will give us a countdown from 0 to 5

for value in range(1, 10):
    # Lower bound is inclusive
    # Upper bound is not inclusive
    print(value)

# The range function also accepts a step interval argument
for value in range(0, 101, 10):
    print(value)