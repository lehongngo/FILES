# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:45:50 2017

@author: LEHONGNGO2012
"""

low=0
hi=100
guessed = False

while not guessed:
    guess= (low+hi)//2
    print('Please think of a number between 0 and 100!')
    print('Is your secret number:'+ ' ' + str(guess) + '?')
    user_input=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'c':
       guessed =True
    elif user_input=='l':
        low=guess
    elif user_input=='h':
        hi=guess
    
    else:
        print('Sorry, I did not understand your input')
print('Game over. Your secret number was:' + str(guess))