def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == 'add':
        return add
    elif operation == 'subtract':
        return subtract


print(calculator("add")(10, 14))