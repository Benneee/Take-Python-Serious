from poker.validators import ThreeOfAKindValidator, PairValidator


class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        
    def is_valid(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()
    
    def valid_cards(self):
        three_of_a_kind_cards = ThreeOfAKindValidator(cards = self.cards).valid_cards()
        pair_cards = PairValidator(cards = self.cards).valid_cards()
        
        all_cards = three_of_a_kind_cards + pair_cards
        all_cards.sort()
        
        return all_cards