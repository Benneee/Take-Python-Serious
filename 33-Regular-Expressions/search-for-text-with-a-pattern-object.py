# Regular expression is a way fo searching for text and matching it with a pattern

import re

pattern = re.compile("flower")

print(type(pattern))

# Python is going to try to look for the text "flower" in "candy"
print(pattern.search("candy"))

match = pattern.search("flower power")
match = pattern.search("a red flower in the field") # To show that regex reads through the full string
print(type(match)) # Match Object

# The Match object has some helpful to identify where the match occurs

# The methods below only run when there is a match object from the search method
# The method "group" returns the string that matches our pattern

if match: # This is a normal convention in regex to avoid errors when there is no match
    print(match.group())

    print(match.start())
    print(match.end())

    print(match.span())