import random


class Card:
    def __init__(self, suit=None, value=None):
        self.suit = suit
        self.value = value

    def present(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        self.cards = []

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit=suit, value=value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [card.present() for card in self.cards]

    def collect_cards(self):
        self.__init__()
