story = "once upon a time";

# Capitalize returns a new string with the first character capitalize
print(story.capitalize());

# If we want the first letters to be capitalized, we can use the method ".title"
# title uses the presence of a space to figure out the first letter of every substring
print(story.title());

# To have all the letters in block form, we can use the method ".upper"
print(story.upper())

# ".lower" does exactly the opposite of upper, however, we don't get to see its effect since our string is all lowercase already
print("Hello".lower());

# ".swapcase" returns a new string where the casing of all the strings are inverted
# All lowercase letters become uppercase letters and vice versa
print(story.swapcase());
print("AbCdE".swapcase())

# We can also chain these methods together
print("BENJAMIN FRANKLIN".lower().title())

# Once again, strings are immutable.
