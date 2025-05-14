numbers = int(input('Enter a number:   ')) 
factorial = 1
for number in range(2, numbers + 1):
	factorial *= number
print(factorial)