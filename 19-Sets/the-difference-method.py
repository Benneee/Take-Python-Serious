# THe difference method returns a new set of the elements contained in the set the method is called on that are not present in the set passed into it
chocolates = { "Mars", "Snickers", "Milky Way" }
sweet_things = { "Mars", "BonBon", "Ptit" }

# Long syntax
# choc_differences = chocolates.difference(sweet_things)
# print(choc_differences)

# Short syntax
choc_differences = chocolates - sweet_things
print(choc_differences)
