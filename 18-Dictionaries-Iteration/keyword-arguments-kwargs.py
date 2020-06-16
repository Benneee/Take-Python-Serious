# **kwargs collects the arguments and creates a dictionary out of them
# kwargs - keyword arguments
# We are not limited by length
# While args bundle sequential arguments to a tuple, kwargs bundles to a dictionary

def collect_keyword_arguments(**kwargs):
    return kwargs


new_dict = collect_keyword_arguments(a=2, b=4, c=6);
print(new_dict)


# If you will be mixing args and kwargs as parameters, the args have to come before kwargs
# Any sequential arguments that don't have keywords before them will be regarded as args

def args_and_kwargs(a, b, *args, **kwargs):
    print(f"The total of the regular arguments is {a + b}")
    print(f"The total of the args tuple is {sum(args)} and its length is {len(args)}")

    # To find the sum of the kwargs values
    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    print(f"The total of the kwargs dictionary values is {dict_total}")


args_and_kwargs(1, 2, 3, 4, 5, 6, x=8, y=9, z=10)