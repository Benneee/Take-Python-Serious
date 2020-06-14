# This method is used to present numeric values in a certain way

# For percentages
print(format(0.5, "%"))

# For only 2 decimal places
print(format(0.5, ".2%"))

# For floats
num = 0.123456789

print(format(num, ".2f"))


# For currency separation
print(format(12345, ","))

# The return value of the format method is a string. It should only be used for aesthetic purposes, i.e presentation, and not data manipulation