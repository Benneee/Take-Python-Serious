class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        return "High Card"

# Duplication is cheaper than the wrong abstraction