# This will only work for simple if/else cases

zip_code = "23401"

if len(zip_code):
    check = "Valid"
else:
    check = "Invalid"


# In ternary operation
# Start with the variable you want to be returned
# followed by the conditions

check = "Valid" if len(zip_code) == 5 else "Invalid"

print(check);
