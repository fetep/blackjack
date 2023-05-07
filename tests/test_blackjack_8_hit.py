#!/usr/bin/env python
# test the strategy for 8 deck, hit on soft17
# https://wizardofodds.com/games/blackjack/strategy/calculator/
# - decks: 4 or more
# - soft 17: dealer hits
# - double after split: allowed
# - surrender: not allowed
# - dealer peek: dealer peeks for blackjack

from blackjack import Actions, Hand, Strategy
from cards import Card, Ranks


class TestHardHand:
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

    # 5: hit against every dealer hand
    def test_player_5(self):
        player = Hand([Card(Ranks._2), Card(Ranks._3)])

        for dealer in self.dealer_hands:
            action = self.strategy.decide(dealer, player)
            assert action == Actions.HIT, f'player hard 5, dealer {dealer.cards[0].rank}'

    # 6: hit against every dealer hand
    def test_player_6(self):
        player = Hand([Card(Ranks._2), Card(Ranks._4)])

        for dealer in self.dealer_hands:
            action = self.strategy.decide(dealer, player)
            assert action == Actions.HIT, f'player hard 6, dealer {dealer.cards[0].rank}'

    # 7: hit against every dealer hand
    def test_player_7(self):
        player = Hand([Card(Ranks._2), Card(Ranks._5)])

        for dealer in self.dealer_hands:
            action = self.strategy.decide(dealer, player)
            assert action == Actions.HIT, f'player hard 7, dealer {dealer.cards[0].rank}'

    # 8: hit against every dealer hand
    def test_player_8(self):
        player = Hand([Card(Ranks._2), Card(Ranks._6)])

        for dealer in self.dealer_hands:
            action = self.strategy.decide(dealer, player)
            assert action == Actions.HIT, f'player hard 8, dealer {dealer.cards[0].rank}'

    # 9: double on dealer 3-6, hit the rest
    def test_player_9(self):
        player = Hand([Card(Ranks._2), Card(Ranks._7)])

        actions = [
            Actions.HIT,    # dealer 2
            Actions.DOUBLE, # dealer 3
            Actions.DOUBLE, # dealer 4
            Actions.DOUBLE, # dealer 5
            Actions.DOUBLE, # dealer 6
            Actions.HIT,    # dealer 7
            Actions.HIT,    # dealer 8
            Actions.HIT,    # dealer 9
            Actions.HIT,    # dealer T
            Actions.HIT,    # dealer A
        ]

        for i, expected_action in enumerate(actions):
            dealer = self.dealer_hands[i]
            action = self.strategy.decide(dealer, player)
            assert action == expected_action, f'player hard 9, dealer {dealer.cards[0].rank}'
