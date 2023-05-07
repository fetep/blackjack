#!/usr/bin/env python

from enum import Enum, auto


class Actions(Enum):
    DOUBLE = auto()
    HIT = auto()
    SPLIT = auto()
    STAND = auto()
