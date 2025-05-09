print('Investment return ')
principal = int(1000)
annual_rate = 7/ 100
amount_deposit = int()
for years in range(1, 31):
	amount_deposit = float(principal * (1 + annual_rate) ** -years)
	print(f'Return for {years} years is {amount_deposit}')
