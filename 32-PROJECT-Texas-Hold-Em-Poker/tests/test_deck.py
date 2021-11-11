import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

# command to run tests in a folder:
# python3 -m unittest <name-of-folder>
class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )


    @patch('random.shuffle')
    def test_shuffles_card_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="8", suit="Diamonds")
        ]
        deck.add_cards(cards)

        deck.shuffle()

        # We expect that shuffle is called once
        # And that it was invoked with some argument
        mock_shuffle.assert_called_once_with(
            cards
        )
