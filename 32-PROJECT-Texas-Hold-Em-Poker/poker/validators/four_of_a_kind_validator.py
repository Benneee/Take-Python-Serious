from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Four of a Kind"
        
    def is_valid(self):
        ranks_with_four_of_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_kind) == 1
    
    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(4)
        cards = [
            card for card in self.cards
            if card.rank in ranks_with_pairs.keys()
        ]
        return cards