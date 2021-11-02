class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        ranks_with_three_of_kind = self._ranks_with_count(3)

        if len(ranks_with_three_of_kind) == 1:
            return "Three of a Kind"

        ranks_with_pairs = self._ranks_with_count(2)

        if len(ranks_with_pairs) == 2:
            return "Two Pair"
        
        if len(ranks_with_pairs) == 1:
            return "Pair"

        
        return "High Card"

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

# setdefault sets a key with its value in the dictionary if the key doesn't previously exist
# Duplication is cheaper than the wrong abstraction