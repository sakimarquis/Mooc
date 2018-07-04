balance = 5000
monthlyPaymentRate = 0.02
annualInterestRate = 0.18

TotalPaid = 0
month = 0
while month < 12:
    MinimumMonthlyPayment = balance * monthlyPaymentRate
    balance -= MinimumMonthlyPayment
    balance +=balance * annualInterestRate / 12
    month += 1
    TotalPaid +=MinimumMonthlyPayment
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(MinimumMonthlyPayment, 2))
    print 'Remaining balance: ' + str(round(balance, 2))
print 'Total paid: ' + str(round(TotalPaid, 2))
print 'Remaining balance: ' + str(round(balance, 2))
