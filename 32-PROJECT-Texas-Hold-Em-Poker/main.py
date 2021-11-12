from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

ayo = Player(name = "Ayo", hand = hand1)
bola = Player(name = "Bola", hand = hand2)
players = [ayo, bola]

game_round = GameRound(deck = deck, players = players)
game_round.play()

#  from main import deck, cards, game_round, hand1, hand2, ayo, bola