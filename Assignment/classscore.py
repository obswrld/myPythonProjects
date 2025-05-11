number_of_students = int(input('Enter Number Of Students:  '))
largest = 0;
name = ' '
for number in range(1, number_of_students + 1):
	names = input('Enter Student name:   ')
	score = int(input('Enter Student score:  '))
	if score < 0 and score > 100:
		print('Please Enter Valid Score:  ')
	if score > largest:
		largest = score
		name = names
print(f'The Student with the highest score is {name} with a score of {largest}')
