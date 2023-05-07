#!/usr/bin/env python

from cards import Ranks
from .enums import Actions

class StrategyException(Exception):
    pass


class Strategy:
    def __init__(self, decks, soft17):
        self.decks = decks
        self.soft17 = soft17

    # returns an action for the player to take
    def decide(self, dealer, player):
        if self.decks == 8 and self.soft17 == Actions.HIT:
            return self.decide_8_hit(dealer, player)

        return StrategyException(f'no strategy for {decks}/{soft17}')

    # strategy for 8 deck, hit on soft17
    def decide_8_hit(self, dealer, player):
        dealer_card = dealer.cards[0]
        player_type, player_value = player.value()

        # if we have 2 cards, check for split & double scenarios
        if len(player.cards) == 2:
            # splits
            if player.cards[0].rank == player.cards[1].rank:
                match player.cards[0].rank:
                    case Ranks._8:
                        # always split 8s
                        return Actions.SPLIT

            # doubles on hard values
            if player_type == 'hard':
                # player hard 9, double on dealer 3/4/5/6
                if player_value == 9:
                    if dealer_card.value() in [3, 4, 5, 6]:
                        return Actions.DOUBLE
                    return Actions.HIT

                if player_value == 11:
                    return Actions.DOUBLE

        # always stand on hard 17+
        if player_type == 'hard' and player_value >= 17:
            return Actions.STAND

        # if we didn't meet any of the above scenarios, just hit
        return Actions.HIT
