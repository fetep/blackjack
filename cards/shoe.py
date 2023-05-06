#!/usr/bin/env python

import random

from .card import Card
from .enums import Ranks, Suits


class ShoeException(Exception):
    pass


class Shoe:
    def __init__(self, decks):
        self.decks = decks
        self.shuffle()

    # re-populate our shoe with the specified number of decks and shuffle
    def shuffle(self):
        # populate self.cards with 1 deck
        self.cards = []
        for rank in Ranks:
            for suit in Suits:
                self.cards.append(Card(rank, suit))

        # expand cards to the number of decks we have
        self.cards *= self.decks

        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            raise ShoeException('out of cards')
        return self.cards.pop()
