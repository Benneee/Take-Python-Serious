address = "Attractive Street, Beverly Hills, CA 90210"

# LHS is inclusive
# RHS is exclusive

# This is a range expression, the RHS value is not added when the output is provided.
print(address[0:3]);
print(address[:3]); # Line 7 can be rewritten like this, only if we are starting from index 0

print(address[19:31]);

# If you use a range value for the RHS that is out of bound/range of the string, python will simply provide you with all the strings up to the end

print(address[-10:])