#!/usr/bin/env python
# test the strategy for 8 deck, hit on soft17
# https://wizardofodds.com/games/blackjack/strategy/calculator/
# - decks: 4 or more
# - soft 17: dealer hits
# - double after split: allowed
# - surrender: not allowed
# - dealer peek: dealer peeks for blackjack

from functools import reduce
from pytest_check import check

from blackjack import Actions, Hand, Strategy
from cards import Card, Ranks


class TestHand:
    dealer_hands = [
        Hand([Card(Ranks._2)]),
        Hand([Card(Ranks._3)]),
        Hand([Card(Ranks._4)]),
        Hand([Card(Ranks._5)]),
        Hand([Card(Ranks._6)]),
        Hand([Card(Ranks._7)]),
        Hand([Card(Ranks._8)]),
        Hand([Card(Ranks._9)]),
        Hand([Card(Ranks.T)]),
        Hand([Card(Ranks.A)]),
    ]
    strategy = Strategy(8, Actions.HIT)

    def compare_actions(self, player, actions):
        if len(actions) != len(self.dealer_hands):
            raise Exception('mismatch between actions and dealer_hands length')

        player_type, player_value = player.value()
        for i, expected_action in enumerate(actions):
            dealer = self.dealer_hands[i]
            action = self.strategy.decide(dealer, player)
            check.equal(
                action,
                expected_action,
                f'{player.value()} against {dealer.cards[0].rank}, should {expected_action.name}',
            )


    def flatten(self, list):
        return reduce(lambda a, b: a + b, list)

    # hard 5: hit against every dealer hand
    def test_hard_5(self):
        player = Hand([Card(Ranks._2), Card(Ranks._3)])
        assert player.value() == ('hard', 5)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 6: hit against every dealer hand
    def test_hard_6(self):
        player = Hand([Card(Ranks._2), Card(Ranks._4)])
        assert player.value() == ('hard', 6)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 7: hit against every dealer hand
    def test_hard_7(self):
        player = Hand([Card(Ranks._2), Card(Ranks._5)])
        assert player.value() == ('hard', 7)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 8: hit against every dealer hand
    def test_hard_8(self):
        player = Hand([Card(Ranks._2), Card(Ranks._6)])
        assert player.value() == ('hard', 8)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 9: double on dealer 3-6, hit the rest
    def test_hard_9(self):
        player = Hand([Card(Ranks._2), Card(Ranks._7)])
        assert player.value() == ('hard', 9)

        self.compare_actions(player, [
            Actions.HIT,     # dealer 2
            Actions.DOUBLE,  # dealer 3
            Actions.DOUBLE,  # dealer 4
            Actions.DOUBLE,  # dealer 5
            Actions.DOUBLE,  # dealer 6
            Actions.HIT,     # dealer 7
            Actions.HIT,     # dealer 8
            Actions.HIT,     # dealer 9
            Actions.HIT,     # dealer T
            Actions.HIT,     # dealer A
        ])

    # hard 10: hit on dealer T/A, double the rest
    def test_hard_10(self):
        player = Hand([Card(Ranks._2), Card(Ranks._8)])
        assert player.value() == ('hard', 10)

        self.compare_actions(player, [
            Actions.DOUBLE,  # dealer 2
            Actions.DOUBLE,  # dealer 3
            Actions.DOUBLE,  # dealer 4
            Actions.DOUBLE,  # dealer 5
            Actions.DOUBLE,  # dealer 6
            Actions.DOUBLE,  # dealer 7
            Actions.DOUBLE,  # dealer 8
            Actions.DOUBLE,  # dealer 9
            Actions.HIT,     # dealer T
            Actions.HIT,     # dealer A
        ])

    # hard 11: double on everything
    def test_hard_11(self):
        player = Hand([Card(Ranks._2), Card(Ranks._9)])
        assert player.value() == ('hard', 11)

        self.compare_actions(player, [Actions.DOUBLE] * 10)

    # hard 12: stay on dealer 4-7, hit on the rest
    def test_hard_12(self):
        player = Hand([Card(Ranks._2), Card(Ranks.T)])
        assert player.value() == ('hard', 12)

        self.compare_actions(player, [
            Actions.HIT,    # dealer 2
            Actions.HIT,    # dealer 3
            Actions.STAND,  # dealer 4
            Actions.STAND,  # dealer 5
            Actions.STAND,  # dealer 6
            Actions.HIT,    # dealer 7
            Actions.HIT,    # dealer 8
            Actions.HIT,    # dealer 9
            Actions.HIT,    # dealer T
            Actions.HIT,    # dealer A
        ])

    # hard 13: stand against bustable dealer hand, hit against made dealer hands
    def test_hard_13(self):
        player = Hand([Card(Ranks._3), Card(Ranks.T)])
        assert player.value() == ('hard', 13)

        self.compare_actions(player, self.flatten([
            [Actions.STAND] * 5,  # dealer 2-6
            [Actions.HIT] * 5,    # dealer 7-A
        ]))

    # hard 14: stand against bustable dealer hand, hit against made dealer hands
    def test_hard_14(self):
        player = Hand([Card(Ranks._4), Card(Ranks.T)])
        assert player.value() == ('hard', 14)

        self.compare_actions(player, self.flatten([
            [Actions.STAND] * 5,  # dealer 2-6
            [Actions.HIT] * 5,    # dealer 7-A
        ]))

    # hard 15: stand against bustable dealer hand, hit against made dealer hands
    def test_hard_15(self):
        player = Hand([Card(Ranks._5), Card(Ranks.T)])
        assert player.value() == ('hard', 15)

        self.compare_actions(player, self.flatten([
            [Actions.STAND] * 5,  # dealer 2-6
            [Actions.HIT] * 5,    # dealer 7-A
        ]))

    # hard 16: stand against bustable dealer hand, hit against made dealer hands
    def test_hard_16(self):
        player = Hand([Card(Ranks._6), Card(Ranks.T)])
        assert player.value() == ('hard', 16)

        self.compare_actions(player, self.flatten([
            [Actions.STAND] * 5,  # dealer 2-6
            [Actions.HIT] * 5,    # dealer 7-A
        ]))

    # hard 17: stand against anything
    def test_hard_17(self):
        player = Hand([Card(Ranks._7), Card(Ranks.T)])
        assert player.value() == ('hard', 17)

        self.compare_actions(player, [Actions.STAND] * 10)

    # hard 18: stand against anything
    def test_hard_18(self):
        player = Hand([Card(Ranks._8), Card(Ranks.T)])
        assert player.value() == ('hard', 18)

        self.compare_actions(player, [Actions.STAND] * 10)

    # hard 19: stand against anything
    def test_hard_19(self):
        player = Hand([Card(Ranks._9), Card(Ranks.T)])
        assert player.value() == ('hard', 19)

        self.compare_actions(player, [Actions.STAND] * 10)

    # hard 20: stand against anything
    def test_hard_20(self):
        player = Hand([Card(Ranks.K), Card(Ranks.T)])
        assert player.value() == ('hard', 20)

        self.compare_actions(player, [Actions.STAND] * 10)
