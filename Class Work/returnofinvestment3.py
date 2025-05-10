investment_amount = int(input('Enter Your Investment Amount:  '))
number_of_years = int(input('Enter Number of Years:  '))
interest_rate = int(input('Enter Rate:  '))
for number_of_years in range(1, number_of_years + 1):
	return_of_investment =  float( investment_amount * ( 1 + (interest_rate / 100)) ** number_of_years + 1)
	print(f'The Amount that will be invested is ₦{investment_amount:.2f} for {number_of_years} years with the interest rate of {interest_rate}% will give a return on 	investment of ₦{return_of_investment:.2f}')
