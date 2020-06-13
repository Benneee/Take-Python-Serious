the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

# for person in the_simpsons:
#     print(f"{person} has a total {len(person)} characters.")

# # In reverse
# for person in the_simpsons[::1]:
#     print(f"{person} has a total {len(person)} characters.")


# Using the built-in reverse method
# THe reversed method does not return a list
# Instead, it returns a generator object
# print(reversed(the_simpsons))


# The syntax for iterating over a generator object is similar to that of the normal list
# But generator objects only store the next element of their elements in memory

# It is very useful when dealing with large lists
for character in reversed(the_simpsons):
    print(f"{character} has a total {len(character)} characters.")