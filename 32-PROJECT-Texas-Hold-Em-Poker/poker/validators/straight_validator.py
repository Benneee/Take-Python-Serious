class StraightValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"
        
    def is_valid(self):
        if len(self.cards) < 5:
            return False

        rank_indexes = [card.rank_index for card in self.cards]
        
        index = 0
        final_index = len(self.cards) - 1
        collection_of_five_straight = []
        
        while index + 4 <= final_index:
            next_five_cards = self.cards[index: index + 5]
            next_five_cards_indices = [
                card.rank_index
                for card in next_five_cards
            ]
            if self._every_element_increasing_by_1(next_five_cards_indices):
                collection_of_five_straight.extend(next_five_cards)
            index += 1
            
        return len(collection_of_five_straight) >= 1
      
    
    def _every_element_increasing_by_1(self, rank_indexes):
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consective_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        return rank_indexes == straight_consective_indexes