values = ["3.14", "9.99", "567.324", "5.678"]
# Produce a list of all the floating numbers
floats = [value.split(".")[1] for value in values]
# print(floats)

name = "Boris"
# Repeat each character in the name variable thrice and let them make up a list
letters = [letter * 3 for letter in name]
# print(letters)

elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
# Produce a list of the lengths of each string in the "elements" list
lengths = [len(el) for el in elements]
# print(lengths)

def destroy_elements(list1, list2):
    outcast = [value for value in list1 if value not in list2]
    print(outcast)


destroy_elements([1,2,3], [1,2])