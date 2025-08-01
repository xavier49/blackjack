#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 20:20:36 2025

@author: xavierlee
"""
import random
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value= value
        
class Deck:
    
    def __init__(self):
        suits = ['h', 's', 'c', 'd']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    
        self.order = [Card(suit, rank, values[rank]) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.order)
        
    def deal(self, receiver):
        card = self.order.pop()
        receiver.hand.add_card(card)
        
        

class Hand:
    
    def __init__(self, cards: list):
        self.cards = cards
        self.value = 0
        
        
        
    def add_card(self, card):
        self.cards.append(card)
        
    def calculate_value(self, receiver, verbose = True):
        self.value = 0
        for card in receiver.hand.cards:
            self.value = self.value + card.value
        if verbose:
            print(f"{receiver}'s hand has value {self.value}")
        return self.value
            
    def show_hand():
        pass
    
class Player:
    
    def __init__(self, stack):
        self.stack = stack
        self.hand = Hand(cards = [])
        
    def __str__(self):
        return("Player")
        
    def hit(self):
        self.hand.add_card()
        self.hand.calculate_value()
        
    
class Game:
    
    def __init__(self, bet, deck, player, dealer):
        self.bet = bet
        self.deck = deck
        self.player = player 
        self.dealer = dealer
        self.result = ""
        
    def start_game(self, player, dealer):
        self.deck.shuffle()
        self.deck.deal(player)
        self.deck.deal(dealer)
        self.deck.deal(player)
        self.player.hand.calculate_value(player)
        self.dealer.hand.calculate_value(dealer)
        
    def playable(self, player, dealer):
        playable = True
        while playable:
            print("Would you like to hit or stand?")
            action = input()
            print(f"Player would like to {action}")
            
            if action.lower() in ("hit", "h"):
                self.deck.deal(player)
                
                if player.hand.calculate_value(player) > 21:
                    print("womp womp you lose give me your money")
                    self.result = "Loss"
                    playable = False
                    
            elif action.lower() in ("stand", "s"):
                playable = False
                
                while dealer.hand.calculate_value(dealer) < 17:
                    self.deck.deal(dealer)
                    
                    if dealer.hand.calculate_value(dealer, verbose = False) > 21:
                        print(f"congrats you just won {self.bet} shmecks")
                        self.result = "Win"
                
                player_value = player.hand.calculate_value(player, verbose = False)
                dealer_value = dealer.hand.calculate_value(dealer, verbose = False)
                
                if player_value > dealer_value:
                    print(f"congrats you just won {self.bet} shmecks")
                    self.result = "Win"
                    
                elif player_value < dealer_value and dealer_value < 21:
                    print("womp womp you lose give me your money")
                    self.result = "Loss"
                    
                else:
                    print("I think this is a push? \n Take your chips back")
                    self.result = "Push"
                    
            else: 
                print("Answer the question")
                
    def endgame(self, bet, player):
        pass
        
        
class Dealer:
    
    def __init__(self):
        self.hand = Hand(cards = [])
        
    def __str__(self):
        return("Dealer")

        