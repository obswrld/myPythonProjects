current_population = 8_000_000_000
growth_rate = 0.0105
years = 100

print(f'{'Years':<10} {'Population':<20} {'Increase':<20}')
print('-' * 50)

initial_population = current_population
double_population = initial_population * 2
quadrible_population = initial_population * 4

for year in range(1, years + 1):
	population_increase = current_population * growth_rate
	anticipated_population = current_population + population_increase

	print(f'{year:<10} {anticipated_population:<20,.0f} {population_increase:<20,.0f}')

	current_population = anticipated_population

	if anticipated_population >= double_population:
		print(f"\nThe population will double in year {year}.")
		double_population = float('inf')

	if anticipated_population >= quadrible_population:
		print("\nThe population will quadriple in year {year}.")
		quadrible_population = float('inf')
	