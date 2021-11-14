from poker.validators import (
    HighCardValidator, 
    NoCardsValidator, 
    PairValidator,
    TwoPairValidator,
    ThreeOfAKindValidator,
    StraightValidator,
    FlushValidator,
    FullHouseValidator,
    FourOfAKindValidator,
    StraightFlushValidator,
    RoyalFlushValidator
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
            ("Royal Flush", RoyalFlushValidator(cards = self.cards).is_valid),
            ("Straight Flush", StraightFlushValidator(cards = self.cards).is_valid),
            ("Four of a Kind", FourOfAKindValidator(cards = self.cards).is_valid),
            ("Full House", FullHouseValidator(cards = self.cards).is_valid),
            ("Flush", FlushValidator(cards = self.cards).is_valid),
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
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
