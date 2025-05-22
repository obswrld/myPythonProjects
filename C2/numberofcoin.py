purchase_price = float(input('Enter the purchase price (up to $1.00):   '))

if 0 < purchase_price <= 100:
	total_paid = 100
	change = round(100 - (purchase_price))
	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0

	quarters = change // 25 
	change = change % 25

	dimes = change // 10
	change = change % 10

	nickels = change // 5
	change = change % 5

	pennies = change
	
	print('Your change is:  ')
	if quarters > 0:
		print(f'{quarters} quater{'s' if quarters > 1 else ' '} ')
	if dimes > 0:
		print(f'{dimes} dime{'s' if dimes > 1 else ' '}')
	if nickels > 0:
		print(f'{nickels} nickel{'s' if nickels > 1 else ' '}')
	if pennies > 0:
		print(f'{pennies} penn{'ies' if pennies > 1 else ' '}')
else:
	print('Please enter a valid price of dollar or less')


	