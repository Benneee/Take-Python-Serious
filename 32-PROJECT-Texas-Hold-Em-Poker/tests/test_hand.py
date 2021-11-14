import unittest
from poker.hand import Hand
from poker.card import Card

class HandTest(unittest.TestCase):
    def test_shows_all_its_cards_in_repr(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            "7 of Clubs, Ace of Diamonds"
        )

    # Because the hand object in a real-life poker game actually starts out without any card
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit ="Spades")
        six_of_clubs = Card(rank = "6", suit ="Clubs")
        
        cards = [
            ace_of_spades,
            six_of_clubs
        ]

        hand = Hand()
        # passing the cards to the card object
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                six_of_clubs,
                ace_of_spades
            ]
        )
