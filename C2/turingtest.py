yes_response = 'yes'
no_response = 'no'
question1 = input('What Is Your problem?  Press Enter after answering:   ')
question2 = input('Have you had this problem before? (Yes or no):  ').strip().lower()
while True:
	if question2 != yes_response and question2 != no_response:
		print('Please Yes or no? Thats all i need Please')
		question2 = input('Have you had this problem before? (Yes or No):  ').strip().lower()
	if question2 == yes_response:
		print('Well You Have It Again.')
		break 
	if question2 == no_response:
		print('You Have It Now.')
		break
