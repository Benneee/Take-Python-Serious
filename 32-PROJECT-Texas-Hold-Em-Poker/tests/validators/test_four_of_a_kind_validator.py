import unittest

from poker.validators import FourOfAKindValidator
from poker.card import Card


class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.three_of_hearts = Card(rank = "3", suit = "Hearts")
        self.three_of_spades = Card(rank = "3", suit = "Spades")
        self.three_of_diamonds = Card(rank = "3", suit = "Diamonds")
        nine = Card(rank = "9", suit = "Spades")
        
        self.cards = [
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            nine
        ]
    
    def test_determines_four_of_the_same_in_the_collection_of_cards(self):
        # Four of a kind = 4 of 1 rank
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
        
    def test_returns_four_cards_of_the_same_rank_from_collection(self):
        validator = FourOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades,
            ]
        )