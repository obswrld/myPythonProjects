largest_one = -888
largest_two = -888
for i in range(10 + 1):
	number = int(input('Enter 10 numbers:  '))
	if number > largest_one and number > largest_two:
		largest_two = largest_one
		largest_one = number
	elif number > largest_two and number != largest_one:
		largest_two = number
print(f'The largest number is {largest_one} and the second largest number is {largest_two}')

	