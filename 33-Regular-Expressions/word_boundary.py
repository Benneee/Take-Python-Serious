import re

# \b word boundary
# "\bt" will only pick matches of that character anywhere the character starts a word
# pattern = re.compile(r"\bt")

# "t\b" will only pick matches of that character anywhere the character ends a word
# pattern = re.compile(r"t\b") # went and bought

# A word boundary asserts the position of a letter within a word

sentence = "I went to the store and bought 5 apples, 4 oranges, and 15 plums."
# print(pattern.findall(sentence))

# \B non-word boundary
# Finds matches where the character does not start the word 
pattern = re.compile(r"\Bt")

# Finds matches where the character does not end the word 
pattern = re.compile(r"t\B")
