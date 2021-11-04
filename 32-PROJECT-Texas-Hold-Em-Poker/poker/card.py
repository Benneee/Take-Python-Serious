class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    
    RANKS = (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )

    @classmethod
    def create_standard_52_cards(cls):
        return [
            cls(rank = rank, suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]
        
        # cards = []
        # for suit in cls.SUITS:
        #     for rank in cls.RANKS:
        #         cards.append(cls(rank = rank, suit = suit))
            
        # return cards

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(
                f"Invalid rank. Rank must be one of the following: {self.RANKS}"
            )

        if suit not in self.SUITS:
            raise ValueError(
                f"Invalid suit. Suit must be one of the following: {self.SUITS}"
            )

        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        current_card_rank_index = self.RANKS.index(self.rank)
        other_card_rank_index = self.RANKS.index(other.rank)
        return current_card_rank_index < other_card_rank_index
