import unittest
from semicolon_bank import accounts,account_balance
from semicolon_bank import accounts,deposit
from semicolon_bank import accounts,withdraw
from semicolon_bank import accounts,check_amount_balance



class Testsemicolon_bank(unittest.TestCase):
	def test_set_up(self):
		global accounts
		accounts = []

	def test_that_deposit_works(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = deposit(accounts, 5000, 50000)
		expected = "your deposited amount is $50000.0, Account Balance is:  $55000.0"
		self.assertEqual(actual, expected)

	def test_that_deposit_cannot_take_negative(self):
		accounts = []
		account_balance(accounts, 5000)
		actual = deposit(accounts, 5000, -5000)
		expected = "Invlaid Amount. Please Deposit a valid amount"
		self.assertEqual(actual, expected)

	def test_that_deposit_cannot_take_in_amount_that_is_not_number(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = deposits(accounts, 50000, "oba")
		expected = "Invalid withdrawal. Amount must be a Number"
		self.assertEqual(actual, expected)


	def test_that_withdraw_works(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, 5000)
		expected = "withdrawn amount is:  $5000.0, withdrawal fee: 100. Account Balance is:  $44900.0"
		self.assertEqual(actual,expected)

	def test_that_withdraw_cannot_take_negative(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, -5000)
		expected = "Invalid withdrawal amount. Please Enter a Valid amount"
		self.assertEqual(actual, expected)

	def test_that_withdraw_cannot_take_amount_that_is_not_multiple_500_or_1000(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, 4333)
		expected = "Invalid Amount, Please Amount must be multiples of 500 or 1000"
		self.assertEqual(actual, expected)

	def test_that_withdraw_cannot_take_amount_that_is_not_number(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, "oba")
		expected = "Invalid withdrawal. Amount must be a Number"
		self.assertEqual(actual, expected)

	def test_that_withdraw_has_charge_fee(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, 5000)
		expected = "withdrawn amount is:  $5000.0, withdrawal fee: 100. Account Balance is:  $44900.0"
		self.assertEqual(actual, expected)

	def test_that_withdraw_amount_higher_than_the_balance(self):
		accounts = []
		account_balance(accounts, 50000)
		actual = withdraw(accounts, 50000, 100000)
		expected = "Sorry, Insufficient Funds"
		self.assertEqual(actual, expected)



	 

	