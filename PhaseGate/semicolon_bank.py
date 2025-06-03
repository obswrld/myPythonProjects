accounts = []

def account_balance(account, balance=0):
	balance = float(balance)
	accounts.append(balance)
	return f'Enter Your account balance:  {balance}'

def check_amount_balance(amount):
	if not amount:
		return "Amount can't be empty"
	if amount.isspace():
		return "Amount can't be empty"

	another_amount = amount.replace('.', ' ', 1)

	if all(number.isdigit() for number in another_amount):

		amount = float(amount)

		if amount == round(amount, 2): 
			return True
		else: 
			return "Invalid amount Please"

def deposit(account, balance, amount):
	try:
		amount = float(amount)
		if amount <= 0:
			return "Invlaid Amount. Please Deposit a valid amount"
		else:
			balance += amount
			return f"your deposited amount is ${amount}, Account Balance is:  ${balance}"
	except ValueError:
		return "Invalid withdrawal. Amount must be a Number"

def withdraw(account, balance, amount):
	try:
		amount = float(amount)
		if amount <= 0:
			return "Invalid withdrawal amount. Please Enter a Valid amount"
		elif amount > balance:
			return "Sorry, Insufficient Funds"
		elif amount % 500 != 0:
			return "Invalid Amount, Please Amount must be multiples of 500 or 1000"
		elif amount > balance * 90 / 100:
			return "Invalid Amount, Please Amount to be withdrawn must not exceed 90% of your account balance"
		else: 
			balance -= amount + 100
			return f"withdrawn amount is:  ${amount}, withdrawal fee: 100. Account Balance is:  ${balance}"
	except ValueError:
		return "Invalid withdrawal. Amount must be a Number"


def goback():
	while input("Press 0 to go back:  ") != '0':
		print('Invalid Number. Press 0 to go back.')

menu_options = True
while menu_options:
	message_menu ="""
Welcome to Semicolon Bank

What will you like to do today?
1=> Enter Your Account Balance
0=> Exit
"""
	print(message_menu)
	try:
		user_input = int(input("Enter the your choice"))
		match user_input:
			case 1:
				user_input1 = input("Enter balance:   ")
				deposit(user_input1)
			case 0:
				user_input3 = input("exit to menu")
				
	
	except ValueError:
		print("Please enter a valid number.")