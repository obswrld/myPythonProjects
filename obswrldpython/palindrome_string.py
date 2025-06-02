def palindrome_string(input_string):
	input_string = input_string.lower()
	return input_string == input_string[::-1]

def palindrome_string1(input_string):
	input_string = input_string.lower()
	length = len(input_string)
	for i in range(length // 2):
		if input_string[i] != input_string[length - 1 - i]:
			return False 
	return True

input_string = "madams"
output_string = palindrome_string1(input_string)
print(output_string)