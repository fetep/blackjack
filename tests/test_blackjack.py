#!/usr/bin/env python

from blackjack import Hand
from cards import Card, Ranks, Shoe, Suits


class TestHand:
    shoe = Shoe(1)
    hand = Hand(shoe)

    def cards(self, *ranks):
        res = []
        for rank in ranks:
            c = Card(rank)
            res.append(Card(rank))

        return res

    def test_creation(self):
        assert len(self.hand.cards) == 2

    def test_hit(self):
        assert len(self.hand.cards) == 2
        self.hand.hit()
        assert len(self.hand.cards) == 3

    def test_value_noaces(self):
        self.hand.cards = self.cards(Ranks._2, Ranks._3)
        assert self.hand.value() == ('hard', 5)

        self.hand.cards = self.cards(Ranks._T, Ranks._4)
        assert self.hand.value() == ('hard', 14)

    def test_value_single_ace(self):
        # soft values (where A can be 1 or 11)
        self.hand.cards = self.cards(Ranks.A, Ranks._4)
        assert self.hand.value() == ('soft', 15)

        self.hand.cards = self.cards(Ranks.A, Ranks._9)
        assert self.hand.value() == ('soft', 20)

        # hard values (where A can only be 1)
        self.hand.cards = self.cards(Ranks.A, Ranks._9, Ranks._7)
        assert self.hand.value() == ('hard', 17)

        self.hand.cards = self.cards(Ranks.A, Ranks._7, Ranks._6)
        assert self.hand.value() == ('hard', 14)

    def test_value_multiple_ace(self):
        self.hand.cards = self.cards(Ranks.A, Ranks.A)
        assert self.hand.value() == ('hard', 12)

        self.hand.cards = self.cards(Ranks.A, Ranks.A, Ranks.A)
        assert self.hand.value() == ('hard', 13)

        self.hand.cards = self.cards(Ranks.A, Ranks.A, Ranks.A, Ranks._4)
        assert self.hand.value() == ('hard', 17)
