import unittest
from unittest.mock import MagicMock, call

from poker.card import Card
from poker.game_round import GameRound


class GameRoundTest(unittest.TestCase):
    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]

        game_round = GameRound(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game_round.deck,
            deck
        )

        self.assertEqual(
            game_round.players,
            players
        )

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game_round = GameRound(
            deck = mock_deck,
            players = players
        )

        game_round.play()

        mock_deck.shuffle.assert_called_once()

    
    def test_deals_two_initial_cards_from_deck_to_each_player(self):
        first_two_cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Spades")
        ]

        next_two_cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "4", suit = "Spades")
        ]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            first_two_cards,
            next_two_cards
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        players = [
            mock_player1,
            mock_player2
        ]

        game_round = GameRound(
            deck = mock_deck,
            players = players
        )

        game_round.play()

        # We are testing that:
        # remove_cards was called
        # that it was called at least twice
        # and that the invocation had the arguments "2" in it
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
        ])

        mock_player1.add_cards.assert_called_with(
            first_two_cards
        )
        mock_player2.add_cards.assert_called_with(
            next_two_cards
        )
