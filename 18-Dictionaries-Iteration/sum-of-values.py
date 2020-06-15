def sum_of_values(a_dict, strings):
    total = 0
    for key, value in a_dict.items():
        if key in strings:
            total += value

    return total

my_dict = { "a": 5, "b": 3, "c": 10 }

total = sum_of_values(my_dict, ["a"])
total2 = sum_of_values(my_dict, ["a", "c"])
total3 = sum_of_values(my_dict, ["a", "c", "b"])
total4 = sum_of_values(my_dict, ["z"])

print(total)
print(total2)
print(total3)
print(total4)
