passes = 0
failures = 0
number_of_students = int(input('Enter amount of Student that has result:  '))

for i in range(number_of_students):
	result_input = int(input('Enter result input:   '))
	if result_input != 1 and result_input != 2: 
		print('Please enter the valid input for pass')
	elif result_input == 1:
		passes = passes + 1
	else: 
		failures = failures + 1
print(f'{passes} passed')
print(f'{failures} failed')
		