import sum 
from unittest import TestCase

class TestSum(TestCase):
	def test_that_getsum_function_exist(self):
		sum.get_sum(5,5)

	def test_that_sum_function_return_correct_answer(self):
		actual = sum.get_sum(7,8)
		expected = 15
		self.assertEqual(actual, expected)
		

	def test_that_sum_function_reject_String_input(self):
		actual = sum.get_sum(a,b)
		expected = print('ValueError')
		self.assertEqual(actual, expected)