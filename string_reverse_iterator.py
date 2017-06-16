# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:40:45 2017

@author: LEHONGNGO2012  
USING FUNCTION CALL IN PYTHON
"""
def listNum():
    
    num = 0
    index =-1
    print('============================List of increasing number================')
    print('INDEX''  ''NUMBER')
    while num < 5:
        num +=1
        index +=1        
        print('%-9s %s' % (index ,num))
        
def listSum(numList):
    
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print('the sum of all elements in List:',listSum([1,3,5,7,9]))    

''' sum list of number
total = 0
for i in range(1,end+1):
     total +=i
     
print(total

'''   
        
def reverseOrder3():
    num = 10
    index = 0
    print('============================List of decreasing number 3================')
    print('INDEX' '  ''NUMBER')
    
    while num >0:        
        if num % 2==0:         
            print('%-9s %s' % (index ,num))
        index = (-num )-index
        num -=1
#for i in range (10, 0,-2):    print reserse list of number skip2
    #print(i)       
       
        
def reverseOrder1():
    num =12
    index =-1
    print('============================List of decreasing number 1================')
    print('INDEX' '  ''NUMBER')
    while num >2:   
        num -= 2
        index +=1
        print('%-9s %s' % (index, num))
       
        
        
def stringReverse():
    string ='abcdefgk'
    print('============================String Reverse===========================')
    print(string, 'after reverse ====>:',string[::-1])
    
    
def stringCount():
    string = 'abcdefgk'
        
    print('============================String Count=============================')
    print('There are total' ,len(string), 'letter in string',string )
    
    
    
def countVowels():
    s = 'nnyeqdospeieaqs'.lower()
    count = 0
    vowels = "aeiou"
    for letter in s:
        if letter in vowels:
            count += 1         
    print('============================ Count Vowels =========================')
    print('There are total vowel aeiou in string s:',(count))  
      
    
def stringSearch():
    string ='abcdefgk'    
    letter =0
    print('============================String Search=============================')
    for letter in range(len(string)):
        if string[letter] == 'b':
          print('There is a letter:' , string[letter],'in string', string)
         
def palindromeCheck():
    print('===========================Palindrome Check=========================')
    string ='radar'
    if str(string) == str((string)[::-1]):
       print('It is a palindrome')    
    else:
        print('It is not Palindrome')
        
   
def main():
    
    listNum()
    listSum([1,2,3,4])
    reverseOrder3()    
    reverseOrder1()
    stringReverse()
    stringCount()
    countVowels()
    stringSearch()
    palindromeCheck()
    
main()
