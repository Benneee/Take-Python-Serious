import unittest

from poker.validators import StraightValidator
from poker.card import Card

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        two = Card(rank = "2", suit = "Spades")
        six = Card(rank = "6", suit = "Hearts")
        self.seven = Card(rank = "7", suit = "Diamonds")
        self.eight = Card(rank = "8", suit = "Spades")
        self.nine = Card(rank = "9", suit = "Clubs")
        self.ten = Card(rank = "10", suit = "Clubs")
        self.jack = Card(rank = "Jack", suit = "Hearts")
        
        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack,
        ]
        
    def test_determines_if_there_are_five_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )