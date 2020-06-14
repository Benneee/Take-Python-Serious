# Much like the JavaScript map function, however, you need to create the function outside the map expression
# It also returns a map object which can be iterated upon, but you'd have to pass it through a list if 
# ...you want a list as the return value
# You also don't need to invoke the function within it

# You use the map function when you want to pass each element of an iterable, e.g list, through an action/ a function

numbers = [2, 4, 6, 8, 20]

def add_one(number):
    return number + 1


convert_to_odd = list(map(add_one, numbers))
# print(convert_to_odd);

animals = ["elephant", "rat", "camel", "giraffe", "chameleon"]
def to_upper(x: str):
    return x.title()

animals_titlecase = list(map(to_upper, animals))

print(animals_titlecase)