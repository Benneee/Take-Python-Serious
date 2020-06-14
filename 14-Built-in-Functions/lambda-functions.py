# Helper function for map and filter
numbers = range(10);

even_numbers = list(filter((lambda num: num % 2 == 0), numbers))
print(even_numbers)

animals = ["elephant", "rat", "camel", "giraffe", "chameleon"]

animals_titlecase = list(map((lambda a: a.title()), animals))

print(animals_titlecase)