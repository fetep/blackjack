#!/usr/bin/env python

from .enums import Ranks

class InvalidCardException(Exception): pass

class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def value(self):
        match self.rank:
            # hand calculator will deal with A being 1 or 11
            case Ranks._A:
                return 1
            case Ranks._2:
                return 2
            case Ranks._3:
                return 3
            case Ranks._4:
                return 4
            case Ranks._5:
                return 5
            case Ranks._6:
                return 6
            case Ranks._7:
                return 7
            case Ranks._8:
                return 8
            case Ranks._9:
                return 9
            case Ranks._T:
                return 10
            case Ranks._J:
                return 10
            case Ranks._Q:
                return 10
            case Ranks._K:
                return 10
            case _:
                return InvalidCardException(f'unknown rank {self.rank}')
        return 10
