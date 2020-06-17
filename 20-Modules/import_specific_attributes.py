# Importing specific attributes from a module can be nice
# However, it's best to avoid this if there will be name collisions

from calculator import add

print(add(5, 10))