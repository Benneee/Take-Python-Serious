import re

pattern = re.compile("flower")

sentence = "There are a lot of flowers in the flowery flower field"

print(pattern.findall(sentence)) # Helpful when you want to search for multiple occurrences within a string

# findall returns a list of all the matches within a string and an empty list when no match is provided
# finditer returns an iterable of match objects from all the occurrences of a pattern within a string

for match in pattern.finditer(sentence):
    print(match)
