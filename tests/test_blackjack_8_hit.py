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
                f'{player.value()} with {dealer.cards[0].rank}, should {action.name}',
            )


    def flatten(self, list):
        return reduce(lambda a, b: a + b, list)

    # hard 5: hit against every dealer hand
    def test_player_hard_5(self):
        player = Hand([Card(Ranks._2), Card(Ranks._3)])
        assert player.value() == ('hard', 5)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 6: hit against every dealer hand
    def test_player_hard_6(self):
        player = Hand([Card(Ranks._2), Card(Ranks._4)])
        assert player.value() == ('hard', 6)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 7: hit against every dealer hand
    def test_player_hard_7(self):
        player = Hand([Card(Ranks._2), Card(Ranks._5)])
        assert player.value() == ('hard', 7)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 8: hit against every dealer hand
    def test_player_hard_8(self):
        player = Hand([Card(Ranks._2), Card(Ranks._6)])
        assert player.value() == ('hard', 8)

        self.compare_actions(player, [Actions.HIT] * 10)

    # hard 9: double on dealer 3-6, hit the rest
    def test_player_hard_9(self):
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
    def test_player_hard_10(self):
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
    def test_player_hard_11(self):
        player = Hand([Card(Ranks._2), Card(Ranks._9)])
        assert player.value() == ('hard', 11)

        self.compare_actions(player, [Actions.DOUBLE] * 10)
