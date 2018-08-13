balance = 4773
annualInterestRate = 0.2

LowestPayment = 0
UnpaidBalance = balance
while UnpaidBalance >0:
    LowestPayment += 10
    UnpaidBalance = balance
    month = 1
    while month <= 12:
        month += 1
        UnpaidBalance = (UnpaidBalance - LowestPayment)*(1+annualInterestRate/12)


print 'LowestPayment: ' + str(LowestPayment)