import unittest

from poker.validators import FullHouseValidator
from poker.card import Card


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.three_of_hearts = Card(rank = "3", suit = "Hearts")
        self.three_of_spades = Card(rank = "3", suit = "Spades")
        self.nine_of_diamonds = Card(rank = "9", suit = "Diamonds")
        self.nine_of_spades = Card(rank = "9", suit = "Spades")
        
        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank="5", suit="Diamonds"),
            self.nine_of_diamonds,
            self.nine_of_spades,
            Card(rank="Queen", suit="Clubs")
        ]
    
    def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another(self):
        # Full house = 3 of 1 rank, 2 of another
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
        
    def test_returns_collection_of_two_cards_of_the_same_rank_and_three_cards_of_the_same_rank(self):
        validator = FullHouseValidator(cards = self.cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_hearts,
                self.three_of_spades,
                self.nine_of_diamonds,
                self.nine_of_spades,
            ]
        )