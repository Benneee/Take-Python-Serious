def height_to_metres(feet, inches):
    total_inches = (feet * 12) + inches # Convert the feet to inches to have similar values
    return total_inches * 0.0254 # The conversion


stats = {
    "feet": 5,
    "inches": 11
}

# To unpack this dictionary as arguments for the function above, we use the double asterisk: **
# The keys within the dictionary need to match the parameters in the method because they are matched literally
# Also, if the function demands two parameters as our function above, your dictionary has to be the same number of key-value pairs
# Hence:
print(height_to_metres(**stats))