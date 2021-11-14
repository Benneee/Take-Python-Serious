import re

# All four methods, match, search, findall and finditer, are also available in the re module
# But we will need to provide two arguments to the method in that case

print(re.search("flower", "Pick flowers in the flower field"))

print(re.match("flower", "flower field"))

print(re.findall("flower", "Pick flowers in the flower field"))

for match in re.finditer("flower", "Pick flowers in the flower field"):
    print(match)