def display_name(age, name):
	for _ in range(age):
		print(name)



#display_name(10, "Helen")
#display_name(name = "Helen", age = 10)


def get_product(*numbers):
	print(numbers)
	product = 1
	for number in numbers:
		print(number)
		product *= number
	return product


print(get_product(3, 6, 5, 6, 7))

print(get_product(4, 3, 7, 9, 10, 15, 23, 21, 12, ))