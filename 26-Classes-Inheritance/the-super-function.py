class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f"{self.name} is enjoying the {food}"

# Subclass
# class Dog(Animal):
#     pass

class Dog(Animal):
  # The super method returns the parent class for us and gives us the ability to add more
  # functionalities to the parent class
  def __init__(self, name, breed):
    super().__init__(name) # This line invokes the dunder init method of the Animal class
    self.breed = breed # This method only exists on Dog objects

class Cat(Animal):
  pass



# Because the Dog class inherits from the animal class, it also inherits it __init__ method
tom = Dog("Tom", "BullDog")
print(tom.eat("bacon"));
print(tom.name)
print(tom.breed)

lucy = Cat('Lucy')
print(lucy.name);
print(lucy.breed) # This line will fail because breed only exists on the Dog object
