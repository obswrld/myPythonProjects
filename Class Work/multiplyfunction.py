def multiply(number1, number2):
	multiply = 0
	number1 = (abs(number1))
	number2 = (abs(number2))

	for i in range(number2):
		multiply += number1
	return multiply


number1 = float(input('Enter First Integer:  '))
number2 = int(input('Enter Second Integer:  '))
result = (multiply(number1, number2))
print(f'multiply:  {result}')