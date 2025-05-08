number = str(input('Enter a number:   '))
reverseNumber = ' '
for letter in number: 
	reverseNumber = letter + reverseNumber 
print(reverseNumber)
if int(number) == int(reverseNumber):
	print('Number is Palindrome')
else: 
	print('Number is not a Palindrome')