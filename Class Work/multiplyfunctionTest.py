import unittest
from multiplyfunction import multiply



class Testmultiplyfunction(unittest.TestCase):
		number2 = 60
		multiply(number1, number2)

	def test_that_multiply_negative_number(self):
		number1 = -90333
		number2 = -63749
		multiply(number1, number2)

	def test_that_mulitiply_function_decimal(self):
		number1 = 2.4
		number2 = 3.4
		multiply(number1,number2)