# setattr is used when the key of part of an object isn't known. 
# It can be use to set the attributes for the object. It is most useful when we can't use the dot syntax to access the attributes of the object as we don't know what exactly to target.

stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        # Since we don't know the keys of the stats dictionary, we can iterate over its content to populate....
        # any object created from the class
        for key, value in stats.items():
            setattr(self, key, value)


bbq = Pizza(stats)
print(bbq.name, bbq.size)

# The dir() method returns a list of all of an object's attributes