# Using the * before parameters name can help you add several parameters
# As long as the exact number of parameters are defined and assigned in the next line of the function
def print_two(*args):
    arg1, arg2 = args;
    print(f'arg1: {arg1}, arg2: {arg2}');


print_two(1,2);