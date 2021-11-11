class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        self.hand.best_rank()