#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 20:44:58 2025

@author: xavierlee
"""

#start game
#ask how much to buy in for
#ask how much to bet
#shuffle and deal
#player has X and dealer shows Y
#calculate value
#hit until stand
#show cards and calculate winner
#calculate payout and update chip count
#ask to play again and how much to bet 
from classes import Card, Deck, Player, Dealer, Game, Hand
import random

def initial():
        print("How much would you like to wager?")
        bet = int(input())
        return Game(bet, deck = Deck(), player = Player(stack, hand = []), dealer = Dealer())

print("Welcome to my blackjack game \n How much would you like to buy in for?")
stack = int(input())
player = Player(stack, hand = [])
dealer = Dealer(hand = [])
current = initial()
current.start_game()