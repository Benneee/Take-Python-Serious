# The elements that aren't shared by both sets will be returned by the symmetric differenc
chocolates = { "Mars", "Snickers", "Milky Way" }
sweet_things = { "Mars", "BonBon", "Ptit" }

# # Long syntax
# not_in_both = chocolates.symmetric_difference(sweet_things)
# print(not_in_both)

# Short syntax
not_in_both = chocolates ^ sweet_things
print(not_in_both)