import random
def multiplication_question():
	num1 = random.randint(1, 9)
	num2 = random.randint(1, 9) 
	question = f'How much is {num1} times {num2}?'
	answer = num1 * num2 
	return question, answer 

def multiplication_game():
	question, correct_answer = multiplication_question()
	while True:
		try: 
			user_answer = int(input(question))
			if user_answer == correct_answer:
				print("Very good!")
				question, correct_answer = multiplication_question()
			else:
				print('No. Please try again.')	
		except valueError:	
			print("Invalid Input. Enter a Number")