class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        return self.hand.best_rank()

    # To ensure our player object can receive new cards
    def add_cards(self, cards):
        # don't need a return here since we just want to give the hand object some cards
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        return False