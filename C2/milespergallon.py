print('Miles Per Gallon')
gallons = int()
miles_per_gallon = int()
sentinel = -1
while gallons != sentinel:
	gallons = int(input("Enter Gallons Used:  "))
	if (gallons == sentinel):
		print('End')
		break;
	else:
		miles = int(input("Enter Miles Driven:  "))
		miles_per_gallons = miles / gallons
		print(f'The miles per gallon for this tank was {miles_per_gallons:,.2f}')
	
	
	