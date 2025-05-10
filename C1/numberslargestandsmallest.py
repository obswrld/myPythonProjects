first_number = int(input('Enter First number:  '))
second_number = int(input('Enter second number:  '))
third_number = int(input('Enter third number:   '))
sum = first_number + second_number + third_number
average = float(first_number + second_number + third_number / 3)
product = first_number * second_number * third_number
smallest = first_number
if second_number < smallest:
	smallest = second_number
if third_number < smallest:
	smallest = third_number
print(f'The sum of the numbers is {sum} and the average of them is {average} and the product is {product} and the smallest is {smallest}.')