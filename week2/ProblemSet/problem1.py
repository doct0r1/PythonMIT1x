"""
Problem 1 - Paying Debt off in a Year

Summery of required math:
	Monthly interest rate= (Annual interest rate) / 12.0
	Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
	Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
	Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for i in range(12):
	print("Month: " + str(i))
	minMonthlyPayment = round((balance * monthlyPaymentRate), 2)
	totalPaid += minMonthlyPayment
	print("Minimum monthly payment: " + str(minMonthlyPayment))
	remainingBalance = balance - minMonthlyPayment
	balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
	print("Remaining balance: " + str(balance))
print("Total paid: " + str(totalPaid))
print("Remaining balance: " + str(balance))