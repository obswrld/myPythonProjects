passes = 0
failures = 0
counter = 0
number_of_students = int(input('Enter amount of Student that has result:  '))

for counter in range(number_of_students):
	while True:
		result_input = int(input(f'Enter result input {counter + 1}:   '))
		if result_input == 1:
			passes = passes + 1
			break
			
		elif result_input == 2:
			failures = failures + 1
			break
			
		else:
			if result_input != 1 and result_input != 2:
				print('Please Enter Valid Number')
print(f'{passes} passed')
print(f'{failures} failed')
		