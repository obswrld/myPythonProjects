def reverse_string(input_string):
	reversed_string = input_string[::-1]
	return reversed_string

def reverse_String1(input_string):
	reversed_string = ""
	for char in input_string:
		reversed_string = char + reversed_string
	return reversed_string 

input_string = "Umbrella"
output_string = reverse_String1(input_string)
print(output_string)

