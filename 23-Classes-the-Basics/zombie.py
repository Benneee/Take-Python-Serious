class Zombie():
    def __init__(self, health = 100, brains_eaten = 5):
        self.health = health
        self.brains_eaten = brains_eaten

bob = Zombie(80, 5)
sally = Zombie(brains_eaten = 3, health=120)
benjamin = Zombie()
