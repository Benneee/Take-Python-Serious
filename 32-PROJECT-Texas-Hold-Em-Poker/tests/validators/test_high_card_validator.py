import unittest

from poker.card import Card

# This type of import below is why we added an __init__.py file in the validators folder, so that all the modules within the validators folder will be accessible within the top directory
from poker.validators import HighCardValidator

# as against this type of import statement
# from poker.validators.high_card_validator import HighCardValidator


class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card(rank= "7", suit= "Clubs"),
            Card(rank= "Ace", suit= "Diamonds")
        ]
        
        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
        
    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card("Ace", "Diamonds")
        
        cards = [
            Card("5", "Spades"),
            Card("8", "Diamonds"),
            Card("10", "Clubs"),
            Card("Queen", "Spades"),
            ace_of_diamonds
        ]
        
        validator = HighCardValidator(cards = cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )