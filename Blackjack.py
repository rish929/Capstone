#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:34:48 2020

@author: rishabhagarwal
"""

import random
playvar = str()
class Card:
    def __init__(self,suit,value,display):
        self.suit = suit
        self.value = value
        self.display = display
    def show(self):
        print(f'{self.display} of {self.suit}')
class Deck:
    def __init__(self):
        self.cardlist = list()
        self.build()
    def build(self):
        for c in ['Spades', 'Hearts', 'Diamonds','Clubs' ]:
            for a in range(1,14):
                
                if a == 1:
                    #value for Ace set as 11 needs to be changed later in the code
                    self.cardlist.append(Card(c,11,'Ace'))
                elif a == 11:
                    self.cardlist.append(Card(c,10,'Jack'))
                elif a == 12:
                    self.cardlist.append(Card(c,10,'Queen'))
                elif a == 13:
                    self.cardlist.append(Card(c,10,'King'))
                else:
                    self.cardlist.append(Card(c,a,(str(a))))
    def showdeck(self):
        for c in self.cardlist:
            c.show()
    def showcard(self):
        a = self.cardlist[0]
        a.show()
    def shuffle(self):
        for i in range(51,0,-1):
            r = random.randint(0,i)
            self.cardlist[i],self.cardlist[r] = self.cardlist[r], self.cardlist[i]
    #def shuffle(self):
        #for i in range(5)
class Game:
    x = 0
    def __init__(self,deckused):
        self.deckused = deckused
        self.hand = list()
        self.handval = int()
        self.dealhand = list()
        self.dealval = int()
        self.playagain = str()
        self.playvar = str()
    def playeranddealerhand(self):
        x = 0
        self.deckused.shuffle()
        for i in range(2):
            self.hand.append(self.deckused.cardlist[i])
        print("In Your Hand")
        for i in self.hand:
            i.show()
            if i.display == 'Ace':
                c = input('What value would you like your ace to be: ')
                c = int(c)
                i.value = c
                x = x+i.value
            else:
                x = x +i.value
        self.handval = x
        print(f'Your hand value is {self.handval}')
        for j in range(2,4,1):
            self.dealhand.append(self.deckused.cardlist[j])
        print("In the Dealer's hands")
        ii = 0;
        for j in self.dealhand:
            if ii == 0:
                j.show()
                ii = ii+1
            else :
                print('Card Face Down')
                break
    def gamecont(self):
        global ij
        ij = 3
        ij2 = 0
        while True:
            ij = ij+1
            d = input('Would you like to hit again: ')
            d = str(d)
            print(d)
            if d.lower() == 'yes':
                self.hand.append(self.deckused.cardlist[ij])
                for j in self.hand:
                    j.show()
                    if j == self.hand[-1]:
                        if j.display == 'Ace':
                            d = input('What value would you like your ace to be: ')
                            d = int(d)
                            j.value = d
                            self.handval = self.handval+j.value
                        else:
                            self.handval = self.handval+j.value
                print(self.handval)
            elif d.lower() == 'no':
                print(f'Your hand value is {self.handval}')
                self.playvar = 'continue'
                break
            if self.handval == 21:
                print("You Win")
                self.playvar = 'win'
                break
            if self.handval>21:
                print('You Lose')
                self.playvar = 'lose'
                break
                
        while self.playvar == 'continue':
                for f in self.dealhand:
                    f.show()
                    if f.display == 'Ace':
                        d = input('What would the dealer like the Ace to be: ')
                        d = int(d)
                        f.value = d
                        self.dealval = self.dealval+f.value
                    else:
                        self.dealval = self.dealval+f.value
                print(f"Dealer Hand Value:{self.dealval}")
                if self.dealval< self.handval:
                    self.dealhand.append(self.deckused.cardlist[ij])
                elif self.dealval == self.handval:
                    print("Push")
                    self.playvar = 'tie'
                elif self.dealval>self.handval:
                    if self.dealval == 21:
                        print('You Lose')
                        self.playvar = 'lose'
                    elif self.dealval>21:
                        print('You Win')
                        self.playvar = 'win'
                    elif self.dealval<21:
                        print('You Lose')
                        self.playvar = 'lose'
    def bankrollfunc(self):
        if self.playvar == str():
            cd = input('How much money is in your bankroll: ')
            cv = input('How much money would you like to put up: ')
            cv = int(cv)
            cd = int(cd)
            self.bankroll = cd
            self.bet = cv
        else:
            self.deckused.shuffle()
            self.hand = list()
            self.handval = int()
            self.dealhand = list()
            self.dealval = int()
            self.playvar = str()
            cv = input('How much money would you like to put up: ')
            cv = int(cv)
            self.bet = cv
            
    def addsub(self):
        if self.playvar == 'win':
            print(f'Winnings:${self.bet}')
            self.bankroll = self.bankroll+self.bet
            print(f'Current Bankroll:${self.bankroll}')
        elif self.playvar == 'tie':
            print(f'Current Bankroll:${self.bankroll}')
        elif self.playvar == 'lose':
            print(f'Losses:${self.bet}')
            self.bankroll = self.bankroll-self.bet
            print(f'Current Bankroll:${self.bankroll}')
    def entiregame(self):
        while True:
            self.bankrollfunc()
            self.playeranddealerhand()
            self.gamecont()
            self.addsub()
            askvar = input('Would you like to play again: ')
            if askvar == 'yes':
                continue
            else:
                break
            
            
        
            
        
        
        
                    
                    
                
                    
                
            
            
            


            
        
            
        
        
            
            
        
        
    

        
        