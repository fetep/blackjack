#!/usr/bin/env python

from cards import Card, Ranks, Shoe, Suits

def test_card_string():
    assert Card(Ranks.A, Suits.D).__str__() == 'Ad'
    assert Card(Ranks._5, Suits.S).__str__() == '5s'

def test_card_value():
    assert Card(Ranks.A, Suits.D).value() == 1
    assert Card(Ranks._5, Suits.D).value() == 5

    for rank in [Ranks.T, Ranks.J, Ranks.Q, Ranks.K]:
        assert Card(rank, Suits.D).value() == 10

def test_shoe_generation():
    assert len(Shoe(1).cards) == 52
    assert len(Shoe(8).cards) == 416

def test_shoe_draw():
    s = Shoe(1)
    card = s.draw()
    assert card not in s.cards

    s = Shoe(8)
    card = s.draw()
    card_left = len([c for c in s.cards if c == card])
    assert card_left == 7

def test_shoe_shuffle():
    s = Shoe(1)
    for _ in range(10):
        s.draw()
    assert len(s.cards) == 42

    s.shuffle()
    assert len(s.cards) == 52
