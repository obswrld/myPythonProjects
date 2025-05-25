import random

def guess_game():
	comp = random.randrange(1, 1000)
	
	guess = 0
	attempts = 0

	while attempts <= 10 and guess != comp and guess != -1:
		guess = int(input("Guess a Number between 1 and 1000 or press -1 to exit:   "))
		attempts += 1

		if guess == -1:
			print('Exiting....')
			break
		elif guess < 1 and guess > 1000:
			print('Please guess the Valid Value')
			continue
	
		if guess == comp:
			print('Correct guess! Well done.')
		elif guess < comp:
			print('Opps to Low! Try Again')
		else: 
			print('Opps to High! Try Again')
	
	if attempts == 10:
		print('You Should be able to do better! Why Should it take more than 10 guesses.')
		break;

guess_game()


	
	