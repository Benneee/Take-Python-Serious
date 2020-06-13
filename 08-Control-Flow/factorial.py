def factorial(num: int):
    if num == 1:
        return num
    product = num * factorial(num - 1)
    # print(product)
    return product


# refactored
def refactorial(num: int):
    return num if num == 1 else (num * refactorial(num - 1)) 

print(factorial(5))
print(refactorial(5))