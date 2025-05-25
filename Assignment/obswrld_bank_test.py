import unittest
from obswrld_bank import accounts,create_account
from obswrld_bank import accounts,deposit
from obswrld_bank import accounts,withdraw
from obswrld_bank import accounts,all_accounts_obswrldbank

class Testobswrld_bank (unittest.TestCase):
	def test_account_created(self):
		create_account("Oba", "09069672905")
		self.assertEqual(1, len(accounts))
	
	def test_create_account_function_works(self):
		create_account("James", "07089872905")
		self.assertEqual(2, len(accounts))

	def test_deposit_functions_with_balance(self):
		name = "Oba"
		balance = 100
		create_account(name, balance)

	def test_deposit_function_works(self):
		balance = 100
		amount = 700
		deposit(balance, amount)

	def test_deposit_function_wiil_not_take_negative_amount(self):
		balance = 100
		amount = -99
		deposit(balance, amount)
	
	def test_deposit_function_will_not_take_zero_amount(self):
		balance = 100
		amount = 0
		deposit(balance, amount)

	def test_deposit_function_will_not_take_a_string_amount(self):
		balance = 100
		amount = 'abc'
		deposit(balance, amount)

	def test_deposit_function_will_be_able_to_allow_float_amount(self):
		balance = 3300.98
		amount = 4550.56
		deposit(balance, amount)

	def test_withdraw_function_with_balance(self):
		name = "oba"
		balance = 5000
		create_account(name, balance)

	def test_withdraw_function_after_balance_will_be_zero(self):
		balance = 5000
		amount = 5000
		withdraw(balance, amount)

	def test_withdraw_function_works(self):
		balance = 4000
		amount = 1000
		withdraw(balance, amount)

	def test_withdraw_function_will_not_take_negative_amount(self):
		balance = 4000
		amount = -1000
		withdraw(balance, amount)
	
	def test_withdraw_function_will_not_take_zero_amount(self):
		balance = 4000
		amount = 0
		withdraw(balance, amount)
	
	def testy_withdraw_function_will_not_take_a_string_amount(self):
		balance = 5000
		amount = "abc"
		withdraw(balance, amount)

	def test_withdraw_function_can_allow_float_amount(self):
		balance = 5000.00
		amount = 3234.45
		withdraw(balance, amount)

	def test_withdraw_function_will_not_take_amount_greater_than_balance(self):
		balance = 5000.43
		amount = 17500.50
		withdraw(balance, amount)

	def test_to_get_all_my_accounts(self):
		create_account("miracle", "9079772905")
		create_account("john", "9059574321")
		customer = all_accounts_obswrldbank()
		self.assertEqual(5, len(accounts)) 
	
	
		
		