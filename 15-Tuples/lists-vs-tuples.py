# Tuples are immutable but if the content is mutable, the content can be directly altered without affecting the overall structure of the tuple. This is the major difference between a tuple and a list
# The other differences are the absence of modifying methods within the tuple class.

animal_classes = (
    ["rat", "lizard", "alligator"],
    ["goat", "cow", "ram"]
)

print(type(animal_classes))

animal_classes[0][0] = "crocodile"
print(animal_classes)