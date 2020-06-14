def collect_stuff(*args):
# The parameter type is a tuple
    print(type(args))
    print(args)
    print(sum(args))



collect_stuff(1,3, 5)

def my_max(*numbers):
    greatest = numbers[0]
    for number in numbers:
        if (number > greatest):
            greatest = number

    return greatest


print(my_max(1, 4, 10, 5, 14, -7))