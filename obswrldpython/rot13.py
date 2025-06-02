def rot13(input_string):
	result = ""
	for char in input_string:
		if 'a' <= char <= 'z':
			result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
		elif 'A' <= char <= 'Z':
			result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
		else: result += char
	return result

input_string = "Hello world"
output_string = rot13(input_string)
print(output_string)