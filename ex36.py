#coding: utf-8

from sys import exit
from random import choice


def start():
    hands = ['rock', 'scissors', 'paper']
    print "Rock-Scissors-Paper game"
    print "%s kill %s, %s kill %s, %s kill %s.\n" % (hands[0], hands[1], hands[1], hands[2], hands[2], hands[0])
    print "The computer can be smart or stupid."
    print "Let's watch they play.\n\n"

    play('', 100)



def play(type, count):
    hands = ['rock', 'scissors', 'paper']

    if type == '':
        player = ['smart', 'stupid']
    else:
        player = ['you', type]
    print "%s %s" % (player[0], player[1])

    i = 0
    score = [0, 0]
    while score[0] + score[1] < count:
        if i == 0:
            h1 = choice(hands)
            h2 = choice(hands)
        else:
            h1_last = h1
            h1 = smart(h1_last)
            h2 = stupid(h1_last)

        r = compare(h1, h2)
        print "%s vs %s = %s" % (h1, h2, r)
        if r != 0:
            if r == 1:
                score[0] += 1
            else:
                score[1] += 1
            print "%s win! score is %d : %d " % (player[r], score[0], score[1])
        i += 1


def hand_win(hand):
    """return what can win hand."""
    if hand == 'rock':
        return 'paper'
    elif hand == 'scissors':
        return 'rock'
    else:
        return 'scissors'

def hand_lose(hand):
    """return what can lose hand."""
    if hand == 'rock':
        return 'scissors'
    elif hand == 'scissors':
        return 'paper'
    else:
        return 'rock'

def compare(h1, h2):
    """win lose draw: return 1 -1 0"""
    if h1 == hand_win(h2):
        return 1
    elif h1 == h2:
        return 0
    else:
        return -1


def stupid(last_hand_opponent):
    """stupid wanna win opponent's last hand."""
    list = [hand_win(last_hand_opponent), hand_win(last_hand_opponent), last_hand_opponent]
    return choice(list)

def smart(last_hand):
    """smart wanna win stupid."""
    list = [hand_lose(last_hand), hand_lose(last_hand), last_hand, hand_win(last_hand)]
    return choice(list)

def dead(why):
    print why, "Bye bye!"
    exi

start()


