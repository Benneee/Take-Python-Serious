def product(a, b):
    return a * b

# Works with either lists or tuples
# The * spreads the elements of the numbers list or tuple to become the two arguments the product function needs
numbers = [3, 5]
numbers = (3, 5)

print(product(*numbers))