def positive_or_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Neither! It's zero"

# print(positive_or_negative(-2))
# print(positive_or_negative(5))
# print(positive_or_negative(0))


def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "divide":
        return a/b
    elif operation == "multiply":
        return a * b
    else:
        return "Please enter a proper mathematical operation"


print(calculate("add", 100, 250))
print(calculate("divide", 100, 250))
print(calculate("subtract", 100, 250))
print(calculate("multiply", 100, 250))
print(calculate("", 100, 250))