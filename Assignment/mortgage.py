print('Mortgage Calculator')

principal = float(input('Enter the principal amount:  '))

interestRate = float(input('Enter the annual interest rate:  '))

durationInYears = float(input('Enter the duration of the loan:  '))

monthlyInterestRate = interestRate / 100 / 12

numberOfMonths = int(durationInYears * 12)

monthlyPayments = float( (principal * monthlyInterestRate) /
					(1 - (1 + monthlyInterestRate) ** -numberOfMonths))

print(' Your Monthly Payment is:  ', monthlyPayments) 

