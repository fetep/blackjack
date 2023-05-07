#!/usr/bin/env python

from cards import Ranks


class Hand:
    def __init__(self, shoe):
        self.shoe = shoe
        self.cards = []
        self.cards.append(self.shoe.draw())
        self.cards.append(self.shoe.draw())

    # add a card and return the new value
    def hit(self):
        self.cards.append(self.shoe.draw())
        return self.value()

    # returns a tuple (value_type, value)
    # value_type is 'hard' or 'soft'
    # value is the integer value of the hand
    def value(self):
        ace_count = len([c for c in self.cards if c.rank == Ranks.A])
        val = sum([c.value() for c in self.cards])
        if ace_count == 0:
            return 'hard', val

        # Card.value() returns 1 for A. We try it as an 11. If adding 10 (making A an 11)
        # would bust us, then it can only be a 1 and it is a hard-value hand
        for _ in range(ace_count):
            # if the ace can only be a 1
            if val + 10 > 21:
                return 'hard', val
            val += 10

        return 'soft', val
