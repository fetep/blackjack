#!/usr/bin/env python

from .enums import Actions
from .hand import Hand
from .strategy import Strategy
from cards import Card, Ranks, Shoe

import os
import random

# 8 deck, hit on soft17
strategy = Strategy(8, Actions.HIT)

total = 0
correct = 0
shoe = Shoe(decks=8)
mode_env = os.getenv('MODE', 'normal')
match mode_env:
    case 'normal':
        mode = ['random']
    case 'hard':
        mode = ['pair', 'soft']
    case 'pair':
        mode = ['pair']
    case 'soft':
        mode = ['soft']
    case _:
        raise Exception(f'unknown MODE: {mode_env}')

while True:
    if shoe.pct_left() < 50:
        print(f'reshuffling')
        shoe.shuffle()

    dealer = Hand(shoe)
    rank = random.choice(list(Ranks))

    match random.choice(mode):
        case 'random':
            player = Hand(shoe)
        case 'pair':
            player = Hand([Card(rank), Card(rank)])
        case 'soft':
            player = Hand([Card(Ranks.A), Card(rank)])
        case _:
            raise Exception('invalid mode')

    # blackjack is boring, skip
    if player.value() == ('soft', 21):
        continue

    print(f'DEALER: {dealer.cards[0].rank}')
    print(f'PLAYER: {player.cards[0].rank} {player.cards[1].rank} [{player.value()}]')

    action = None
    while action is None:
        action_input = input('Action? ')
        match action_input.lower():
            case 'd':
                action = Actions.DOUBLE
            case 'h':
                action = Actions.HIT
            case 'p' | 'sp':
                action = Actions.SPLIT
            case 's':
                action = Actions.STAND
            case _:
                print('invalid action; d=double h=hit p=split s=stand')

    correct_action = strategy.decide(dealer, player)
    total += 1

    if correct_action == action:
        msg = 'correct'
        correct += 1
    else:
        msg = f'incorrect, correct action: {correct_action.name}'

    pct = round(correct / total * 100, 1)
    print(f'{msg} | {correct}/{total} correct [{pct}%]\n')
