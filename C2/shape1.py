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
	for k in range(1, 11, 1):
		print(f'{'*':>1}', end=' ')

	print()

print()

for i in range(1, 11):
	for j in range(11, -1):
		print(f'{' ':>1}', end=' ')
	for k in range(9, -11):
		print(f'{'*':>1}', end=' ')
	print()
print()
