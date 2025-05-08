number = int(input('Enter a Number:  '))
reverseNumber = int(0)
temp = number
while temp > 0:
		remainder = int(temp % 10)
		reverseNumber = reverseNumber * 10 + remainder
		temp = temp / 10
if number == reverseNumber:
	print('Number is a palindrome')
else:
	print('Number is not a Palindrome')
				


