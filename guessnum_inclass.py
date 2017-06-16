# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:14:46 2017

@author: LEHONGNGO2012
"""

low=0
hi=100
guessed= False


while not guessed:
    guess=(low+hi)/2
    print('Is your secret number:'+' ' + str(guess))      
    user_input=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")      
    
    if user_input== 'c' :   
      guessed=True
    
    elif user_input == 'h' : 
      hi=guess
      
    elif user_input =='l':
      low=guess
      
    else:
     print('Sorry, I did not understand your input')
