from poker.validators import FiveCardsInARowValidator

class StraightValidator(FiveCardsInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"
        
    def is_valid(self):
        return len(self._collections_of_five_straight_cards) >= 1
    
    def valid_cards(self):
        return self._collections_of_five_straight_cards[-1]
    