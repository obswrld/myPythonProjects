for i in range(1, 11):
	for j in range(1, i):
		print(f'{'*':>1}', end =' ')
	print()

print()


for i in range(10, 1, - 1):
	for j in range(1, i):
		print(f'{'*':>1}', end= ' ')
	print()


print()


for i in range(1, 11):
	for j in range(1, i):
		print(f'{' ':>1}', end =' ')
	for k in range(11 - i):
		print(f'{'*':>1}', end =' ')

	print()

print()


for i in range(1, 11):
	for j in range(10, i):
		print(f'{' ':>1}', end =' ')
	for k in range(i, 11):
		print(f'{'*':>1}', end =' ')
	print()

print()




