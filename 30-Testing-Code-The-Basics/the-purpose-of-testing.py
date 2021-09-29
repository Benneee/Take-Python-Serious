# Testing primer

def add(x, y):
    # The assert keyword will evealuate to none if the conditions are met
    assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integers"
    return x + y

print(add(3, 5))
# print(add(3, '5'))

# Assertions will be made about the code to expect that it meets certain conditions so our code does not break