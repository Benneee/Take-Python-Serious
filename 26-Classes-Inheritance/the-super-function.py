class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        return f"{self.name} is enjoying {food}"


class Dog(Animal):
    pass


tom = Dog("Tom")

print(tom.eat("bacon"));