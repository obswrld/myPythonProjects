for a in range(1, 20):
	for b in range(a, 20):
		for c in range(b, 20):
			if c**2 == a**2 + b**2:
				print(f'{c} = {a} + {b}')