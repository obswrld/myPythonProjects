def product(*args):
	result = 1
	for number in args:
		result *= number
	return result

print(product(4,3))
		