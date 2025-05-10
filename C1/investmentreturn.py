print('Investment Return')
principal = int(1000)
annualRate = 7 / 100
numberOfYears1 = 10
numberOfYears2 = 20
numberOfYears3 = 30

amountDeposit1 = float(principal * (1 + annualRate) ** -numberOfYears1)
amountDeposit2 = float(principal * (1 + annualRate) ** -numberOfYears2)
amountDeposit3 = float(principal * (1 + annualRate) ** -numberOfYears3)


print('The Amount Of Money Returned after 10 years:  ', amountDeposit1)
print('The Amount Of Money Returned after 20 years:  ', amountDeposit2)
print('The Amount Of Money Returned after 30 years:  ', amountDeposit3)