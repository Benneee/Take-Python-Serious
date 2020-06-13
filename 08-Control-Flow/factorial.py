def factorial(num: int):
    if num == 1:
        return num
    product = num * factorial(num - 1)
    print(product)
    return product


print(factorial(5))