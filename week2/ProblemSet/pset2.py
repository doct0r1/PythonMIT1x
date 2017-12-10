"""
Author: Mustafa Jamal

Uncomment the code out to run it on your machine.
"""

# balance = 3329
changableBalance = balance
# annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lowestPayment = 0

while changableBalance > 0:
    changableBalance = balance
    lowestPayment += 10
    for i in range(12):
        changableBalance = changableBalance - lowestPayment
        changableBalance = changableBalance + (changableBalance * monthlyInterestRate)
        # print(changableBalance)

print('Lowest Payment ' + str(lowestPayment))