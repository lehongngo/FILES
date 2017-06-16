# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 22:54:19 2017

@author: LEHONGNGO2012
"""

s = "supercalafragilisticexpialadocious"
temp= []
temp.append([0])
ls=[]
len_ls=0

for i in range (0,len(s)-1):
    if s[i+1] >= s[i]:        
        temp.append(s[i+1])        
    else: 
        if len(temp)>len(ls):
            ls = temp        
        temp =[]
        temp.append(s[i+1])
if len(temp) > len(ls):
        ls = temp
print('Longest substring in alphabetical order is:',' '.join(ls))
        