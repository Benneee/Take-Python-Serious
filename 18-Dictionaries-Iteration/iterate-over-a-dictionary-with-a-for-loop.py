chinese_food = {
    "Sesame Chicken": 9.99,
    "Ribs": 7.99,
    "Fried Rice": 1.99
}

# for key in chinese_food:
#     print(f"The food is {key} and its price is ${chinese_food[key]}")

pounds_to_kilogram = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398
}

# for p in pounds_to_kilogram:
#     print(f"{p} pounds is equal to {pounds_to_kilogram[p]} kilograms")

def count_of_value(a_dict, val: int):
    count = 0
    for _, number in a_dict.items():
        if val == number:
            count += 1

    return count

my_dict = {
    "a": 5,
    "b": 3,
    "c": 5
}

count = count_of_value(my_dict, 3)
# print(count)
