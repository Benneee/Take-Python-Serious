from poker.validators import (
    HighCardValidator, 
    NoCardsValidator, 
    PairValidator,
    TwoPairValidator
)

class Hand():
    """
     A class collects a list of 
     cards and provides some methods to 
     evaluate the quality of the cards in
     the player's hand, so to say.

     ---

     Attribute
        cards: str[]
    """
    def __init__(self):
        # We will move the sorting to the add_cards method
        # copy = cards[:]
        # copy.sort()
        # self.cards = copy
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    @property
    def _rank_validations_from_best_to_worst(self):
        return(
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", self._straight),
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            ("Pair", PairValidator(cards = self.cards).is_valid),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards = self.cards).is_valid)
        )

    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            # Three of a kind, self._three_of_a_kind
            name, validator_func = rank
            if validator_func():
                return name

    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        if not is_straight_flush:
            return False

        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal

    def _straight_flush(self):
        # Straight flush is a combo of straight & flush
        return self._flush() and self._straight()

    def _four_of_a_kind(self):
        ranks_with_four_of_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_kind) == 1

    def _full_house(self):
        return self._three_of_a_kind() and PairValidator(cards = self.cards).is_valid()

    def _flush(self):
        suits_that_occur_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items() if suit_count >= 5
        }

        return len(suits_that_occur_5_or_more_times) == 1

    
    def _straight(self):
        if len(self.cards) < 5:
            return False

        rank_indexes = [card.rank_index for card in self.cards]
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consective_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        return rank_indexes == straight_consective_indexes

    def _three_of_a_kind(self):
        ranks_with_three_of_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_kind) == 1

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

# setdefault sets a key with its value in the dictionary if the key doesn't previously exist
# Duplication is cheaper than the wrong abstraction