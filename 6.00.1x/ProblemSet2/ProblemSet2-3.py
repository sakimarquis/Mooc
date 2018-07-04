balance = 4773
annualInterestRate = 0.2

LowestPayment = 0
UnpaidBalance = balance
high = (balance * (1 + annualInterestRate / 12) ** 12) / 12
low = balance / 12

while UnpaidBalance > 0 or UnpaidBalance < -0.01:
    month = 1
    UnpaidBalance = balance
    while month <= 12:
            month += 1
            UnpaidBalance = (UnpaidBalance - LowestPayment)*(1+annualInterestRate/12)
    if UnpaidBalance < 0:
        high = LowestPayment
    else:
        low = LowestPayment
    LowestPayment = (high + low) / 2.0

print 'LowestPayment: ' + str(round(LowestPayment,2))