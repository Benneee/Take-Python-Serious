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

for player in players:
    print(f"{player.name} receives a {player.hand}")
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_strings = " and ".join(hand_cards_strings)
    
    print(f"{player.name} has a {hand_name} with a {hand_cards_strings}.")
    
winning_player = max(players)
print(f"The winner is {winning_player.name}")

#  from main import deck, cards, game_round, hand1, hand2, ayo, bola