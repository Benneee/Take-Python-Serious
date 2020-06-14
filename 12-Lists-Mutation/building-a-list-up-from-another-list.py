power_numbers = [4, 8,15, 16, 23, 25]

def squares(numbers):
    sq_power_numbers = []
    for num in numbers:
        sq_power_numbers.append(num ** 2)

    return sq_power_numbers;

print(squares(power_numbers))