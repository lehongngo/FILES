# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:01:40 2017

@author: LEHONGNGO2012
"""

def isPrime(x):

    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def isEven(x):
    
    for i in range(2,x):              
        if x%i == 0:
            return True       
    return False   

def listsum(x,y):
   
    return x+y
        
def test_Even():
    assert isEven(6),[2,4,6,8,10]    
    
def test():
    assert isPrime(5),[2,3,5]
    
def test_sum():
    assert listsum(2,3)==(5)