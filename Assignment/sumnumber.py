value = input('Enter number:  ')
if value.isdigit():
	number = int(value)
	if  0 < number <= 10000:
		sum = 0
		for i in str(number):
			sum += int(i)
		print(f'sum is:  {sum}')
	else:
		print("Invalid Input")
else:
	print("Enter valid input")