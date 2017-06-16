# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
balance= 42
annualInterestRate= 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
minMonthlyPayment = 0
updatedMonthlyBal = 0
monthlyinterest = 0
month = 0
pay = 0

print('Test Case 1:')
print('Balance:' + str(round(balance,2)))
print('Anual Interest Rate:' + str(round(annualInterestRate,2)))
print('Monthly Payment Rate:' + str(round(monthlyPaymentRate,2)))
print('*******************************')

while month < 12:
    minPayment= balance * monthlyPaymentRate
    updatedMonthlyBal= balance - minPayment
    monthlyinterest = 0.2/12 * updatedMonthlyBal
    pay +=minPayment
    balance = updatedMonthlyBal + (monthlyInterestRate * updatedMonthlyBal)
    month +=1   
    
   
    print('month:' + str(month),'Remaining balance:' + str(round(updatedMonthlyBal,2)))
   


