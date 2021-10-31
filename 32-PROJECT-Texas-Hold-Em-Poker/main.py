from poker.card import Card
from poker.deck import Deck

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

#  from main import deck, cards