from random import choice

class HandRules(object):
    def __init__(self):
        self.hands = ['rock', 'scissors', 'paper']

    def hand_random(self):
        """return a random hand."""
        return choice(self.hands);

    def hand_win(self, hand):
        """return what can win hand."""
        if not (hand in self.hands):
            print "wrong hand: %s" % hand
            exit(1)

        if hand == 'rock':
            return 'paper'
        elif hand == 'scissors':
            return 'rock'
        else:
            return 'scissors'
    
    def hand_lose(self, hand):
        """return what can lose hand."""
        if not (hand in self.hands):
            print "wrong hand: %s" % hand
            exit(1)

        if hand == 'rock':
            return 'scissors'
        elif hand == 'scissors':
            return 'paper'
        else:
            return 'rock'

    def hand_compare(self, h1, h2):
        """win lose draw: 1 -1 0"""
        if h1 == self.hand_win(h2):
            return 1
        elif h1 == h2:
            return 0
        else:
            return -1
