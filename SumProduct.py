number1 = int(input('Enter first integer:  '))
number2 = int(input('Enter second integer:  '))
number3 = int(input('Enter third integer:  '))

sum = number1 + number2 + number3
average = float(number1 + number2 + number3 / 3)
product = number1 * number2 * number3

smallest = number1

if number2 < smallest:
	smallest = number2
if number3 < smallest:
	smallest = number3

largest = number1 

if number2 > largest:
	largest = number2
if number3 > largest:
	largest = number3



print('The sum of the integers:  ', sum)
print('The average of the integers:  ', average)
print('The product of the integers:  ', product)
print('The Smallest number is:  ', smallest)
print('The Largest number is:  ',largest)