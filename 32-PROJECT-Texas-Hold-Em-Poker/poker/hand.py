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
            
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator, 
        NoCardsValidator, 
    )
    
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy
    
    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (
                    index,
                    validator.name,
                    validator.valid_cards()
                )