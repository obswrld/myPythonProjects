sum = int(0)
product = int(1)
total = (0)
smallest = float('inf')
largest = float('-inf')
for number in range(1, 5):
	number = int(input('Enter Number:   '))
	sum = sum + number
	product = product * number
	total = total + number
	if number < smallest:
		smallest = number
	if number > largest:
		largest = number
average = float(total / 3)
print(f'The sum of the integers is {sum} and the product is {product} and the average {average} while the smallest number was {smallest} and the largest number is {largest}')
	