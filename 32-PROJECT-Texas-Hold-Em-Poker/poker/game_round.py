class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        self.deck.shuffle()

        for player in self.players:
            # Each player needs to get two cards at the beginning of the poker game - rules
            self.deck.remove_cards(2)
