# So you can put a 3rd number in the slice syntax. The 3rd number defines the number of steps in which to slice

# How many characters you want to jump forward by when moving from one position to the next...

alphabet = 'abcdefghijklmnopqrstuvwxyz';

print(alphabet[0:10:2])

# Same thing written in 3 ways
print(alphabet[0:26:3])
print(alphabet[::3])
print(alphabet[0::3])

# Reverse the whole string
print(alphabet[::-1])

