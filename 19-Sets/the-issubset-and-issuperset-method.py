# A subset is part of a larger set
# A superset is one that contains all of the elements of the other set and some more the other set doesn't contain

a = { 1, 2, 4 }
b = { 1, 2, 3, 4, 5 }

# part_of_b = a.issubset(b)
part_of_b = a < b # can use < or <=

# makes_up_b = a.issuperset(b)
makes_up_b = a > (b) # can use > or >=

print(part_of_b)
print(makes_up_b)