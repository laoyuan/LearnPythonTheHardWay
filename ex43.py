#coding: utf-8
"""
石头剪子布 机机对战
"""


from sys import exit
from random import choice
from ex43_hand import HandRules

class Game(object):
    def __init__(self):
        self.hands = ['rock', 'scissors', 'paper']
        print "Rock-Scissors-Paper game"
        print "%s kill %s, %s kill %s, %s kill %s." % (self.hands[0], self.hands[1], self.hands[1], self.hands[2], self.hands[2], self.hands[0])
        print "The computer can be smart or stupid."
        print "Let's watch they play.\n"
    
    
    def play(self, p1, p2, count):
        print "'%s' vs '%s' * %d, start" % (p1.player_name, p2.player_name, count)
        hand_rules = HandRules()

        i = 1
        score = [0, 0]
        while score[0] + score[1] < count:
            if i == 1:
                h1 = hand_rules.hand_random()
                h2 = hand_rules.hand_random()
            else:
                h1_last = h1
                h1 = p1.this_hand(h1_last)
                h2 = p2.this_hand(h1_last)
    
            r = hand_rules.hand_compare(h1, h2)
            print "%d. %s : %s = %s" % (i, h1, h2, r),
            if r != 0:
                if r == 1:
                    score[0] += 1
                else:
                    score[1] += 1
                print "  %d : %d " % (score[0], score[1]),
            print ""
            i += 1
        if score[0] > score[1]:
            print "Winer is %s" % p1.player_name
        elif score[0] < score[1]:
            print "Winer is %s" % p2.player_name
        else:
            print "Draw game!"



class Player(object):

    def __init__(self, which):
        self.players = ['stupid', 'smart']
        self.player_name = which
        if not (which in self.players):
            print "player %s not found" % which
            exit(1)

    def this_hand(self, last_hand):
        hand_rules = HandRules()
        if self.player_name == self.players[0]:
            list = [hand_rules.hand_win(last_hand), hand_rules.hand_win(last_hand), last_hand]
        else:
            list = [hand_rules.hand_lose(last_hand), hand_rules.hand_lose(last_hand), hand_rules.hand_win(last_hand), last_hand]
        return choice(list)



game = Game();
player1 = Player('stupid')
player2 = Player('smart')
count = 100

game.play(player1, player2, count)




