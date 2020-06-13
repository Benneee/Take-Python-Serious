def product(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        total = 1
        for number in numbers:
            total = total * number

        return total

print(product([1,2,3,4]))