def greatest_number(numbers):
    if len(numbers) == 1:
        return numbers[0]

    else:
        greatest = numbers[0]
        for num in numbers:
            if num > greatest:
                greatest = num

        return greatest


print(greatest_number([1, 3, 8, 10, 4]))
print(greatest_number([-1, -3, -8]))