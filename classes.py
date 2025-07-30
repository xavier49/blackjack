#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 20:20:36 2025

@author: xavierlee
"""

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value= value
        
class Deck:
    import random
    
    def __init__(self):
        suits = ['h', 's', 'c', 'd']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    
        self.order = [Card(suit, rank, value[rank]) for suit in suits for rank in ranks]
    
    def shuffle():
        #randomize cards in deck
        self.order = random.shuffle(self.order)
    def deal(receiver):
        #take top card off deck
        

class Hand:
    def __init__(self):
        
    def add_card():
        
    def calculate_value(hole_cards):
    
    def show_hand():
        
class Player:
    def __init__(self, stack, hand):
        self.stack = stack
        
    def hit():
        hand.add_card()
        hand.calculate_value()
    def stand():
        
    
class Game:
    def __init__(self, bet):
        self.bet = bet
        
    def start_game():
        deck.shuffle()
        deck.deal(player)
        deck.deal(dealer)
        deck.deal(player)
        
        

        