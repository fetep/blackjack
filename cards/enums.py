#!/usr/bin/env python

from enum import Enum, auto


class Ranks(Enum):
    _A = auto()
    A = _A
    _2 = auto()
    _3 = auto()
    _4 = auto()
    _5 = auto()
    _6 = auto()
    _7 = auto()
    _8 = auto()
    _9 = auto()
    _T = auto()
    T = _T
    _J = auto()
    J = _J
    _Q = auto()
    Q = _Q
    _K = auto()
    K = _K

    # remove the leading '_'
    def __str__(self):
        return f'{self.name[-1]}'


class Suits(Enum):
    CLUBS = auto()
    C = CLUBS
    DIAMONDS = auto()
    D = DIAMONDS
    HEARTS = auto()
    H = HEARTS
    SPADES = auto()
    S = SPADES

    # suit is represented by a single lowercase char
    def __str__(self):
        return f'{self.name[0].lower()}'
