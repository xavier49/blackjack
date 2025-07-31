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
    
        self.order = [Card(suit, rank, value[rank]) for suit in suits for rank in ranks]
    
    def shuffle(self):
        #randomize cards in deck
        random.shuffle(self.order)
    def deal(self, receiver):
        #take top card off deck
        card = self.order.pop()
        receiver.hand.add_card(card)

class Hand:
    def __init__(self, cards):
        self.cards = cards
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(hole_cards):
        value = 0
        for card in cards:
            value = value + card.value
        print(f"Your hand has value {value}")
    def show_hand():
        
class Player:
    def __init__(self, stack, hand):
        self.stack = stack
        self.hand = hand
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
        
class Dealer:
    def __init__(self, hand):
        self.hand = hand

        