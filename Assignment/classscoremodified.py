number_of_students = int(input('Enter Number Of Students:  '))
first_highest_score = 0
first_name = ' '
second_highest_score = int() 
second_name = ' '
for number in range(1, number_of_students + 1):
	names = input('Enter Student name:   ')
	score = int(input('Enter Student score:  '))
	if score < 0 and score > 100:
		print('Please Enter Valid Score:  ')
	if score > first_highest_score and score > second_highest_score:
		second_highest_score = first_highest_score
		first_highest_score = score
		second_name = first_name = names
		first_name = score
	elif score > second_highest_score:
		second_highest_score = score
		second_name = names
print(f'The Student with the highest score is {first_name} with a score of {first_highest_score}')
print(f'The Student with the second highest score is {second_name} with a score of {second_highest_score}')
