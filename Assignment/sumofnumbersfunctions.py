def sum_of_numbers(number):
	return sum(int(i) for i in str(number))

number = input('Enter a number:  ')
result = sum_of_numbers(number)
print(f'sum is: {result}')