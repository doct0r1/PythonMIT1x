"""
Author: Mustafa Jamal

Uncomment the code out if you gonna run it on your machine
"""

# balance = 42
# annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
# monthlyPaymentRate = 0.04

for i in range(12):
    balance = round(balance - (balance * monthlyPaymentRate), 2)
    balance = round(balance + (monthlyInterestRate * balance), 2)
    # print('Month ' + str(i+1) + ' Remaining Balance = ' + str(balance))

# print('')
print('remaining Balance = ' + str(balance))
