#!/usr/bin/env python

from blackjack import Hand
from cards import Card, Ranks, Shoe, Suits


class TestHand:
    def cards(self, *ranks):
        res = []
        for rank in ranks:
            c = Card(rank)
            res.append(Card(rank))

        return res

    def test_creation(self):
        hand = Hand(Shoe(1))
        assert len(hand.cards) == 2

    def test_hit(self):
        hand = Hand(Shoe(1))
        assert len(hand.cards) == 2
        hand.hit()
        assert len(hand.cards) == 3

    def test_value_noaces(self):
        hand = Hand(self.cards(Ranks._2, Ranks._3))
        assert hand.value() == ('hard', 5)

        hand = Hand(self.cards(Ranks._T, Ranks._4))
        assert hand.value() == ('hard', 14)

    def test_value_single_ace(self):
        # soft values (where A can be 1 or 11)
        hand = Hand(self.cards(Ranks.A, Ranks._4))
        assert hand.value() == ('soft', 15)

        hand = Hand(self.cards(Ranks.A, Ranks._9))
        assert hand.value() == ('soft', 20)

        # hard values (where A can only be 1)
        hand = Hand(self.cards(Ranks.A, Ranks._9, Ranks._7))
        assert hand.value() == ('hard', 17)

        hand = Hand(self.cards(Ranks.A, Ranks._7, Ranks._6))
        assert hand.value() == ('hard', 14)

    def test_value_multiple_ace(self):
        hand = Hand(self.cards(Ranks.A, Ranks.A))
        assert hand.value() == ('hard', 12)

        hand = Hand(self.cards(Ranks.A, Ranks.A, Ranks.A))
        assert hand.value() == ('hard', 13)

        hand = Hand(self.cards(Ranks.A, Ranks.A, Ranks.A, Ranks._4))
        assert hand.value() == ('hard', 17)
