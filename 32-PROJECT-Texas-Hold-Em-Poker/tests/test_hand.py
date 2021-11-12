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

    def test_figures_out_no_card_is_best_rank(self):
        hand = Hand()
        self.assertEqual(
            hand.best_rank(),
            "No Cards"
        )

    def test_figures_out_high_card_is_best_card(self):
        cards = [
            Card(rank= "Ace", suit= "Diamonds"),
            Card(rank= "7", suit= "Clubs")
        ]

        hand = Hand()

        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_card_is_best_card(self):
        cards = [
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "Ace", suit= "Clubs")
        ]

        hand = Hand()

        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "5", suit= "Clubs"),
            Card(rank= "Ace", suit= "Clubs"),
            Card(rank= "King", suit= "Hearts"),
            Card(rank= "King", suit= "Diamonds")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card("King", "Clubs"),
            Card("King", "Clubs"),
            Card("King", "Clubs"),
            Card("Ace", "Spades"),
            Card("5", "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )

    def test_figures_out_straight_is_the_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs"),
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_best_rank_when_flush(self):
        # >= Five cards with the same suit = Flush
        cards = [
            Card(rank = rank, suit = "Hearts")
            for rank in ["2", "5", "8", "10", "Ace"]
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_out_full_house_is_best_rank(self):
        # Full house = 3 of 1 rank, 2 of another
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )
    
    def test_figures_out_four_of_a_kind_is_best_rank(self):
        # Four of a kind = 4 of 1 rank
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "3", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_out_straight_flush_is_best_rank(self):
        # Straight flush = 5 of the same suit
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_out_royal_flush_is_best_rank(self):
        # Royal flush is a straight flush that ends in an ace, which means it has to start with a rank of 10
        cards = [
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )