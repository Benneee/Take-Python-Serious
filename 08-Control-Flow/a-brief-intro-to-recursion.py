def count_down_from(num: int):
    start = num
    while start > 0:
        print(start)
        start -=1

# count_down_from(5)

# Recursion happens when a function calls itself within its own body

# Establish a base case
# The base case can be a conditional to avoid an unending loop
def count_down_from(num: int):
    if num <= 0:
        return

    print(num)
    count_down_from(num - 1)

# count_down_from(5)
