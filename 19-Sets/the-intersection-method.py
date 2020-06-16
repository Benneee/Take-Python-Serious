# The intersection method is invoked on one set and it accepts another set as an argument, it returns a new set which contains the elements that appear in both sets

chocolates = { "Mars", "Snickers", "Milky Way" }
sweet_things = { "Mars", "BonBon", "Ptit" }

# Long syntax
# similarities = chocolates.intersection(sweet_things)

# Shorthand syntax
similarities = chocolates & sweet_things
print(similarities)


values = {3.0, 5.0, 6.0, 7.0}
more_values = {3, 4, 7}
same_values = values & more_values
print(more_values)