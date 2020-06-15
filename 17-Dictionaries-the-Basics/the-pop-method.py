con = {
    "a": "b",
    "b": "c",
    "c": "d"
}

value =  con.pop("b", 2000)
# print(value)

def delete_keys(a_dict, strings):
    for value in strings:
        if value in a_dict:
            deleted_keys = a_dict.pop(value, None)

    return a_dict

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

letters = ["A", "C"]

print(delete_keys(my_dict, letters));