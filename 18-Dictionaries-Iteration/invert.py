def invert(a_dict):
    new_dict = {}
    for key, value in a_dict.items():
        new_dict[value] = key

    return new_dict

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5
}

new_dict = invert(my_dict)
print(new_dict)