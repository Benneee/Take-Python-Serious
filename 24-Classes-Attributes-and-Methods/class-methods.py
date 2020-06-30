# Class methods are methods defined on the class itself.

class SushiPlatter():
    def __init__(self, salmon, shrimp, tuna, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp

    # A class method - its parameter is the entire class
    @classmethod
    def lunch_special_A(cls):
        return cls(salmon=2, tuna=2, shrimp=4, squid=0)


ben = SushiPlatter(salmon=8, tuna=4, shrimp=5, squid=10)
print(ben.salmon)

lunch_guy = SushiPlatter.lunch_special_A()
print(lunch_guy.salmon)