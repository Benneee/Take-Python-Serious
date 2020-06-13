# A function that returns the sum of all the odd numbers of a list
def odd_sum(numbers):
    if len(numbers) == 1:
        if numbers[0] % 2 == 1:
            return numbers[0]
        else:
            return "No odd number in list"
    else:
        total = 0
        for number in numbers:
            if number % 2 == 1:
                total += number
        
        return total

print(odd_sum([1, 2, 4, 5, 6, 7]))