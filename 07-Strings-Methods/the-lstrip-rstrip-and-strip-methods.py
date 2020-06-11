# lstrip strips whitespace from the left hand side
# rstrip strips whitespace from the right hand side

empty_space = "        content      "

regular_stripped = empty_space.strip();
right_stripped = empty_space.rstrip()
left_stripped = empty_space.lstrip()

# We can use the len function to see if these strings are different after applying the strip functions on them
print(len(empty_space)) # 21

print(len(regular_stripped)) # 7
print(len(right_stripped)) # 15
print(len(left_stripped)) # 13

# All of these methods can collect a parameter for a substring to be stripped off the string
website = "www.python.org"

remove_w = website.lstrip("w");
remove_org = website.rstrip(".org")

print(remove_w)
print(remove_org)

# The characters do not have to be in any order, the methods just look for them and remove them accordingly
# However, it mainly focuses on either sides of a string, use any of the strip methods

# If you don't feed any argument to the methods, it will default to stripping whitespace
# Also, you have to reassign the value of your string to modify the original string
remove_domain = website.strip("worg.");
print(remove_domain)