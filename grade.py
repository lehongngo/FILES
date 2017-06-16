# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:47:19 2017

@author: LEHONGNGO2012
"""

score = float(input('Please Enter score:'))
grade = None

if score >= 90:
    grade ='A'
    print ('great job you get:' + str(grade))
elif score >=80:
    grade ='B'
    print ('Your grade is:' + str(grade))
elif score >=70:
    grade='C'
    print ('Your grade is :' + str(grade))  
else:
    grade='F'
    print ('your grade is:' + str(grade)) 
    



                  
       
    