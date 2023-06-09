#!/usr/bin/env python

from cards import Card, Ranks, Shoe, Suits


class TestCards:
    def test_string(self):
        assert Card(Ranks.A, Suits.D).__str__() == 'Ad'
        assert Card(Ranks._5, Suits.S).__str__() == '5s'

    def test_value(self):
        assert Card(Ranks.A, Suits.D).value() == 1
        assert Card(Ranks._5, Suits.D).value() == 5

        for rank in [Ranks.T, Ranks.J, Ranks.Q, Ranks.K]:
            assert Card(rank, Suits.D).value() == 10


class TestShoe:
    def test_generation(self):
        assert len(Shoe(1).cards) == 52
        assert len(Shoe(8).cards) == 416

    def test_draw(self):
        s = Shoe(1)
        card = s.draw()
        assert card not in s.cards

        s = Shoe(8)
        card = s.draw()
        card_left = len([c for c in s.cards if c == card])
        assert card_left == 7

    def test_pct_left(self):
        s = Shoe(1)
        for _ in range(26):
            s.draw()
        assert s.pct_left() == 50

    def test_shuffle(self):
        s = Shoe(1)
        for _ in range(10):
            s.draw()
        assert len(s.cards) == 42

        s.shuffle()
        assert len(s.cards) == 52
