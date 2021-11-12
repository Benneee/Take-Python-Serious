class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()

    def _shuffle_deck(self):
        self.deck.shuffle()
    
    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            # Each player needs to get two cards at the beginning of the poker game - rules
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)
