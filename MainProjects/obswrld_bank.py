accounts = []
def create_account(name, phone_number, balance=0.0):	
	account = [name, phone_number]
	accounts.append(account)
	return account

def deposit(balance, amount):
	try:
		amount = float(amount)
		if amount <= 0:
			print('Invalid deposit amount. Please enter a positive value.')
			return balance
		else: 
			balance += amount
			print(f'Deposited ${amount}, New Balance: ${balance}')
	except ValueError:
		print('Invalid Number. Amount must be a number.')	
		return balance

def withdraw(balance, amount):
	try: 
		amount = float(amount)
		if amount <= 0:
			print('Invalid withdraw. Please enter a positive number,')
			return balance
		elif amount > balance:
			print('Insufficient Funds.')
		else: 
			balance -= amount
			print(f'Withrawed ${amount}, New Balance: ${balance}')
	except ValueError:
		print('Invalid Number. Amount must be a number.')
		return balance

def all_accounts_obswrldbank():
	return accounts

def identify_accounts(identifier, identifier1):
	for account in accounts:
		if account[0] == identifier or account[1] == identifier1:	
			return account
	return None
	
