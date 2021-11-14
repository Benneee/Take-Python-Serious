import re

pattern = re.compile("flower")

match = pattern.match("flower power")

if match:
    print(match.group())

    print(match.start())
    print(match.end())

    print(match.span())


# Search will find a match anywhere in the string
# Match will only find at the beginning
print(pattern.match("a red flower")) # This will return None