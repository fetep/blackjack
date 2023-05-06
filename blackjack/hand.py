#!/usr/bin/env python

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

    # returns a tuple (string, int)
    # string is 'hard' or 'soft', int is the value of the hand
    def value(self):
        return 'hard', 18
