# PS2.1
# PAYING THE MINIMUM

balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
monthly_interest_rate = annualInterestRate / 12.0
monthly_payment = monthlyPaymentRate * balance
new_balance = (balance - monthly_payment) * (1 + monthly_interest_rate)
paid_total = 0

for month in range(1, 13):
	monthly_payment = monthlyPaymentRate * balance
	balance = (balance - monthly_payment) * (1 + monthly_interest_rate)
	paid_total += monthly_payment

	print ('Month: %d \n Minimum monthly payment: %g \n Remaining balance: %g' % (month, round(monthly_payment, 2), round(balance, 2)))

print ("Total paid: " + str(round(paid_total, 2)))
print ("Remainig Balance: " + str(round(balance, 2)))

