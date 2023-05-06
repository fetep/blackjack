#!/usr/bin/env python

from cards import Card, Ranks, Shoe, Suits

def x_test_hand_creation():
    assert Card(Ranks._A, Suits.D).__str__() == 'Ad'
    assert Card(Ranks._5, Suits.S).__str__() == '5s'

