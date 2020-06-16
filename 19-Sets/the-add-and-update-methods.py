# Once a set has been created, there are two ways to add new elements to it

# The add method
disney_characters = { "Mickey Mouse", "Minnie Mouse", "Elsa" }

disney_characters.add("Ariel")
print(disney_characters)

# The update method
# This method collects an iterable and attempts to add them to the set
disney_characters.update(["Donald Duck", "Goofy"])
print(disney_characters)

disney_characters.update(("Simba", "Mickey Mouse", "Timon"))
print(disney_characters)