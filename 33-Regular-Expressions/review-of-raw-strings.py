# Raw strings are strings printed out exactly how they are written

print("\tTake a look. There's a tab and line break\n right here.") # => Python interprets this with respect to the escape characters
print(r"\tTake a look. There's a tab and line break\n right here.") # => while raw string is preceded by a "r" like the "f" in the format string