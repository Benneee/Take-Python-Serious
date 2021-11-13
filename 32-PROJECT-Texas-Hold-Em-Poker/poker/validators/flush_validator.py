class FlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"
        
    def is_valid(self):
        return len(self._suits_that_occur_5_or_more_times) == 1
    
    def valid_cards(self):
        cards = [
            card
            for card in self.cards
            if card.suit in self._suits_that_occur_5_or_more_times
        ]
        return cards[-5:]
    
    @property
    def _suits_that_occur_5_or_more_times(self):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items() 
            if suit_count >= 5
        }
    
    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts