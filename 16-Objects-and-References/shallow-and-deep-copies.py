# Because some objects are easily mutable, an obvious solution is to do a copy of that object before any operation is 
# ...carried out on it. 
# There are however two types of copies: Shallow Copy amd Deep Copy

# A shallow copy creates a new object, read list, and inserts references to all the elements within the object, read list, for all the objects found in the original list
# Shallow copying is a great choice if the list is not multidimensional.

from copy import copy
from copy import deepcopy

# There are three ways a shallow copy can be done - SHALLOW COPY

# 1. List slicing
# a = [1, 2, 3]
# b = a[:]
# print(a == b)
# print(a is b) # False because b is a copy of a and not actually a

# # 2. The copy method
# c = a.copy()
# print(a == c)
# print(a is c) # False because c is a copy of a and not actually a

# # 3. Using the copy method from the copy module
# d = copy(a);
# print(d == a)
# print(d is a) # False because c is a copy of a and not actually a


# DEEP COPY
numbers = [1, 2, 4]
a = [1, numbers, 5];
b = deepcopy(a)

print(a == b)
print(a is b)
print(a[1] is b[1])
