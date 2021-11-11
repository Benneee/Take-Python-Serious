from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])

ayo = Player(name = "Ayo", hand = hand1)
bola = Player(name = "Bola", hand = hand2)

#  from main import deck, cards, hand1, hand2, ayo, bola