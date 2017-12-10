"""
Author: Mustafa Jamal

Comment first 2 lines out to run you code on your machine
"""

# balance = 999999
# annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
lowBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
changeableBalance = balance
lowestPayment = 0

while abs(changeableBalance) >= 0.01:
    changeableBalance = balance
    guess = (lowBound + upperBound) / 2
    for i in range(12):
        changeableBalance = changeableBalance - guess
        changeableBalance = changeableBalance + (changeableBalance * monthlyInterestRate)

    if changeableBalance < 0:
        upperBound = guess
    elif changeableBalance > 0:
        lowBound = guess

print("Lowest Payment: ", round(guess, 2))
