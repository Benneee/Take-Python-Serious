# An easier way to inject strings into a string
# This is new though, might not work well with python versions younger than 3.6
name = "Benneee"
adjective = "silly"
noun = "clown"
mad_libs_with_keywords = f"{name} laughed at the {adjective} {noun}."

print(mad_libs_with_keywords)

# You can also run mathematical evaluations within the curly brackets
print(f"2 + 3 is {2 + 3}")