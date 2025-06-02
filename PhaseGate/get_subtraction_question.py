import random

def get_subtraction_question():
	number1 = random.randint(0, 9999)
	number2 = random.randint(0, number1)
	return f"What is {number1} - {number2}?", number1 - number2

def main():
	questions = 0
	max_questions = 10

	while questions < max_questions:
		question, correct_answer = get_subtraction_question()
		print(question)

		attempts = 2
		while attempts > 0:
			user_answer = int(input("Your answer:  "))

			if user_answer == correct_answer:
				print("Very good!")
				break
			else:
				attempts -= 1
				if attempts > 0:
					print(f"Opps! you have {attempts} attempts left. Try again:  ")
				else: 
					print(f"I'm sorry. No attempts left.")
		questions += 1
		print("The next question is:  ")

if __name__ == "__main__":
	main()