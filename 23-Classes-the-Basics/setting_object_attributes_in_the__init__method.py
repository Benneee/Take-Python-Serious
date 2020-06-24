'''
    The goal of OOP is to ensure consistency across objects created from the same class.
    The objects can have different values for state but it's ideal if they have the same methods and attributes
'''
class Guitar():
    def __init__(self, wood):
        self.wood = wood


acoustic = Guitar("Obeche")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)