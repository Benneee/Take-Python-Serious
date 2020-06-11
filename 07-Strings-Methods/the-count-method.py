# Check how many times a character appears within a string

word = "queueing"

print(word.count("e"));
print(word.count("u"));
print(word.count("q"));

# Caveat
# Python when given a substring of more than one character searches for the literal match of the characters when using the count method and it will only give back the number of times the values appear together
# However, if they are not sequential in the original string, the count method would return 0

print(word.count("ue")); # 2
print(word.count("en")) # 0

# However, we can also do this
print(word.count("u") + word.count("e")); # This will give us the sum of the number of appearance of both substrings in the original string

