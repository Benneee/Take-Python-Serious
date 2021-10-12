# List comprehension is designed to create a list from an existing list
# The logic comes before the normal for-loop syntax
# The result is packed into the preferred data structure, hence the list at the boundaries
numbers = [3, 5, 7, 8, 9]
squares = [number ** 2 for number in numbers]

# print(squares)

rivers = ["Nile", "Niger", "Ikogosi"]
# Create a list that contains the length of all the elements in rivers list (Using list comprehension)
river_lengths = [len(river) for river in rivers]
# print(river_lengths)

expressions = ["lol", "rofl", "lmao"]
# Return a list with all the characters above in uppercase
expressions_upper = [e.upper() for e in expressions]
print(expressions_upper)

profiles = [
    {'email': 'ali@yopmail.com', 'first_name': 'ali', 'last_name': 'bara'},
    {'email': 'sam@yopmail.com', 'first_name': 'sam', 'last_name': 'una'},
    {'email': 'tom@yopmail.com', 'first_name': 'tom', 'last_name': 'riddle'},
    {'email': 'bimbo@yopmail.com', 'first_name': 'bimbo', 'last_name': 'thomas'}
]

emails = [obj['email'] for obj in profiles]
print('emails: ', emails)