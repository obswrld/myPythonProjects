def vowel_count(input_string):
	count = 0
	vowel = 'aeiouAEIOU'
	for char in input_string:
		if char in vowel:
			count += 1
	return count

input_string = "Elephant"
output_string = vowel_count(input_string)
print(output_string)