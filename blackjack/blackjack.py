#!/usr/bin/env python

from cards import Shoe
from hand import Hand

class Blackjack:
    def __init__(self, decks):
        self.shoe = Shoe(decks)

shoe = Shoe(decks=8)
dealer = Hand(shoe)
player = Hand(shoe)
print(f'dealer cards: {[str(c) for c in dealer.cards]}')
print(f'player cards: {[str(c) for c in player.cards]}')
