# The following methods all return boolean values
print('winter'.islower()); 

print("BEN".isupper());

# These methods check through all the characters of the string to ensure their condition is met
# The quirk with it is when you have multiple substrings as it will always return false in that aspect

print("The Name".istitle());
print("The name".istitle()); # False


# The isalpha method checks if all the characters of a string are actually alphabets
print("name".isalpha())
# whether or not they are all alphabets

# Complementary to isalpha method, we have isnumeric, which checks if all the characters of a string are numbers
print("51".isnumeric()) # If the values within the quotes are actually numbers, yes, isnumeric confirms they are numbers

print("Area51".isnumeric()) # False

# isalnum to check if a string is a mixture of alphabets and numbers
print("Area51".isalnum()) # True

# the isspace method checks if a string is actually just spaces
print(" ".isspace())