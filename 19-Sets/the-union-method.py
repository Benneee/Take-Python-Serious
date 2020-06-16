# The union method is invoked on one set and it accepts another set as an argument, it returns a new set which contains a combination of elements that appear in both sets

chocolates = { "Mars", "Snickers", "Milky Way" }
sweet_things = { "Mars", "BonBon", "Ptit" }

# Long Syntax
# together = chocolates.union(sweet_things)
# print(together)

# SHort syntax
together = chocolates | sweet_things
print(together)
