estimated_number = 1;
factorial = 1
for number in range(1, 10):
	factorial *= number
	estimated_number += 1 / factorial
print(f'The estimated value is {estimated_number}')