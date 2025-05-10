number = int(0)
sqaure = int(0)
cube = int(0)
limit = 5

print(f'{'number':<10}{'Square':<10}{'Cube':<10}')

for number in range(0, limit + 1):
	square = number** 2
	cube = number** 3
	print(f'{number:<10}{square:<10}{cube:<10}')
