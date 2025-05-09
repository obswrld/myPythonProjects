while True:
	number = int(input('Enter a postive number:  '))
	if number < 1:
		print('Please Enter a positive Number')
	else: 
		for i in range(number, 0, -1):
			print(i)
		print('Blast Off!')