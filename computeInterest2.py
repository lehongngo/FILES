# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:20:09 2017

@author: LEHONGNGO2012
"""
balance = 3329
initBalance = balance
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyUnpaidBal= 0
updatedMonthlyBal = 0
month = 0
minPay = 10

print('Balance:' + str(round(balance,2)))
print('Annual Interest Rate:' + str(round(annualInterestRate,2)))

def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    balance = initBalance
    minPay +=10
    month = 0
    calculate(month, balance, minPay, monthlyInterestRate)
print('Lowest Payment: ' + str(minPay))