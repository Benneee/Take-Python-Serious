# The shuffle method collects a list as its argument and shuffles its content
# The list will be mutated in place - meaning it will be changed
# The shuffle method itself will always return 'None'


from random import shuffle
from copy import copy

characters = ['Warrior', 'Druid', 'Hunter', 'Rogue', 'Mage']
print(characters)
# In other not to lose the original list, we can create a copy of the list and pass its copy to the shuffle method instead
# We can create copies of the list using 3 methods
clone = characters[:] # Method 1: using a range
print(clone)

clone_two = characters.copy() # Method 2: using the list's copy method
print(clone_two)

clone_three = copy(characters) # Method 3: using the copy method off the copy module
print(clone_three)

shuffle(clone)
print(clone)

shuffle(clone_two)
print(clone_two)

shuffle(clone_three)
print(clone_three)