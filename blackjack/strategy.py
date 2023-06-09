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

        # by default, we stand (final return). the following logic is to decide if we should
        # do something other than hit

        # it's easiest to think about the dealer hand value by assuming any card we can't
        # see is valued at 10 (T, J, Q, K).
        if dealer_card.rank == Ranks.A:
            dealer_value = 21
        else:
            dealer_value = 10 + dealer_card.value()

        # if we have 2 cards, check for split & double scenarios
        if len(player.cards) == 2:
            # deal with pairs
            if player.cards[0].rank == player.cards[1].rank:
                match player.cards[0].rank:
                    case Ranks._2 | Ranks._3 | Ranks._7:
                        # split against dealer 17 and below
                        if dealer_value <= 17:
                            return Actions.SPLIT
                    case Ranks._4:
                        # split against dealer 15/16
                        if 15 <= dealer_value <= 16:
                            return Actions.SPLIT
                    case Ranks._6:
                        # split against dealer 16 and below
                        if dealer_value <= 16:
                            return Actions.SPLIT
                    case Ranks._9:
                        # always split except against 17 (we win) or 20/21 (take less risk)
                        if dealer_value not in [17, 20, 21]:
                            return Actions.SPLIT
                    case Ranks._8 | Ranks._A:
                        # always split
                        return Actions.SPLIT

            # double down when we have a hard value hand
            if player_type == 'hard':
                match player_value:
                    case 9:
                        # player hard 9, double on dealer 3/4/5/6
                        if 13 <= dealer_value <= 16:
                            return Actions.DOUBLE
                    case 10:
                        # double 10 except against T/A
                        if dealer_value < 20:
                            return Actions.DOUBLE
                    case 11:
                        # always double 11
                        return Actions.DOUBLE

        # soft value hands
        # general rules:
        # - always stand on soft 20
        # - always stand on soft 19, except dealer 6 (get money in, double)
        # - soft 18 or less, always double against 4/5/6
        # - soft 17/18 can double against a 3
        # - soft 17 can double against a 2
        if player_type == 'soft':
            if 13 <= player_value <= 16:
                # double against the worst dealer hands, hit against the rest
                if dealer_value in [14, 15, 16]:
                    return Actions.DOUBLE
                else:
                    return Actions.HIT
            elif player_value == 17:
                # double against anything up to a dealer 16, hit the rest
                if dealer_value <= 16:
                    return Actions.DOUBLE
                else:
                    return Actions.HIT
            elif player_value == 18:
                # double against most bad dealer hands but not scary ones (12)
                if dealer_value in [13, 14, 15, 16]:
                    return Actions.DOUBLE

                # since we're losing to dealer 19/20, hit
                if dealer_value in [19, 20]:
                    return Actions.HIT

                # since we're losing to dealer 19/20, hit
                if dealer_value in [19, 20]:
                    return Actions.HIT
            elif player_value == 19 and dealer_value == 16:
                # 19 is good enough to stay with, except for a dealer 16 (double)
                return Actions.DOUBLE
            elif player_value == 20:
                # always stand on soft 20
                return Actions.STAND

        # hard value hands
        elif player_type == 'hard':
            if player_value <= 11:
                # if we haven't hit the above double scenarios, hit any hand 11 or less.
                return Actions.HIT
            elif player_value == 12:
                # hit against a dealer 2/3
                if dealer_card.value() in [2, 3]:
                    return Actions.HIT

            # if we are less than 17 and expected dealer value is >= 17, hit
            if player_value < 17 and dealer_value >= 17:
                return Actions.HIT

        # if we didn't meet any of the above scenarios, just stand
        return Actions.STAND
