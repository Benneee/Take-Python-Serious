import unittest

from poker.validators import ThreeOfAKindValidator
from poker.card import Card


class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        five = Card("5", "Clubs")
        self.king_of_clubs = Card("King", "Clubs")
        self.king_of_diamonds = Card("King", "Diamonds")
        self.king_of_hearts = Card("King", "Hearts")
        ace = Card("Ace", "Spades")
        
        self.cards = [
            five,
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            ace
        ]
    
    def test_validates_that_card_have_exactly_three_of_the_same_ranks(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
        
    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts
            ]
        )