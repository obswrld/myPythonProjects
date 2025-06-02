import unittest
from vowel_count import vowel_count

class Testvowel_count(unittest.TestCase):
	def test_that_vowel_count_exist(self):
		input_string = "Elephant"
		vowel_count(input_string)

	def test_that_count_counts_vowel_in_word(self):
		input_string = "Republic Oba"
		output_string = 5
		self.assertEqual(vowel_count(input_string), output_string)

	def test_that_counts_upper_case(self):
		input_string = "acAdEmics"
		output_string = 4
		self.assertEqual(vowel_count(input_string), output_string)

	def test_that_vowel_counts_lower_case(self):
		input_string = "AcademIcs"
		output_string = 4
		self.assertEqual(vowel_count(input_string), output_string)

	
	