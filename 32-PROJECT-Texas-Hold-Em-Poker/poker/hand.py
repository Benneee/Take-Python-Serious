class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        card_rank_counts = {}

        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1

        for rank_count in card_rank_counts.values():
            if rank_count == 2:
                return "Pair"

        return "High Card"

# setdefault sets a key with its value in the dictionary if the key doesn't previously exist
# Duplication is cheaper than the wrong abstraction