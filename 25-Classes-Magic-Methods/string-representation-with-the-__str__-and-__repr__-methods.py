# Python has no way of knowing how you want to represent your object as string, if you create an object from a class and print said object, it shows you the object's class and its location in the memory of your machine

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # So when we ask for an object,say with the print function, Python looks for the string representation of that object using its class, by looking for dunder str method, and afterwards, if it can't find that, a dunder repr method
    # string
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # representation
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'



c = Card("Ace", "Spades")
print(c)
print(repr(c))