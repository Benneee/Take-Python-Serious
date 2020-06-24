class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    # All instance methods must take self as a single parameter
    def roar(self):
        print(f"{self.name} just roared: Raaaaaar!")
    
    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon.")

    def take_damage(self, amount):
        self.health -= amount




squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 110)

charmander.roar()
squirtle.describe()

charmander.take_damage(20)
print(charmander.health)