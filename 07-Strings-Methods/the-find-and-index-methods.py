word = "character"

# The find and index methods return the same values, however, the latter fails or crashes the program when a substring is not found

# find method is much more friendlier in terms of unfounded substrings
print(word.find("r")); # Returns the index of the first appearance of the string
print(word.find("s")); # Returns -1 if string is not found

# The index method crashes the program if it doesn't find a substring
print(word.index("r"));
print(word.index("s"))