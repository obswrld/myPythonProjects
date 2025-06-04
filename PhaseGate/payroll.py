class Employee:
	def __init__(self, name, hourly_work, pay_rate, gross_pay, federal_tax_rate, state_tax_rate):
		self.name = name
		self.hourly_work = hourly_work
		self.pay_rate = pay_rate
		self.gross_pay = gross_pay
		self.federal_tax_rate = federal_tax_rate
		self.state_tax_rate = state_tax_rate

	def calculate_net_pay(self, hours_worked):
		pay_rate = self.pay_rate
		gross_pay = self.pay_rate * hours_worked 
		federal_tax = self.federal_tax_rate * gross_pay / 100
		state_tax_rate = self.state_tax_rate * gross_pay / 100
		net_pay = (federal_tax + state_tax) - gross_pay
		return net_pay

def main():
	employee_map = {}
	
	while True:
		name = input("Enter employee name(ot type 'exit' to finish): ")
		if name.lower() == 'exit':
			break
		if name in employee_map:
			print("Employee already exists. Please enter a unique name.")
			continue
		while True:
			try: 
				hourly_work = float(input("Enter numbers of hours worked:   "))
				if hourly_work <= 0 and hourly_work > 12:
					print("Hourly pay cannot be negative or higher than the normal here. Please enter a valid amount")
					continue
				break
			except ValueError:
				print("Invalid input. Please enter a numeric value for hourly pay.")

		while True:
			try:
				pay_rate = float(input("Enter hourly payrate:  "))
				if pay_rate < 0:
					print("Hourly pay rate cannot be negative. Please enter a valid amount")
					continue
				break
			except ValueError:
				print("Invalid input. Please enter a numeric value for hourly pay.")

		while True:
			try:
				gross_pay = float(input("Enter gross pay:  "))
				if gross_pay < 0:
					print("Gross rate cannot be negative. Please enter a valid amount")
					continue
				break
			except ValueError:
				print("Invalid input. Please enter a numeric value for hourly pay.")


		while True:
			try:
				federal_tax_rate = float(input("Enter federal tax rate:   "))
				if federal_tax_rate < 0:
					print("Please enter a valid rate.")
					continue
				break
			except ValueError:
				print("Invalid input. Please enter a numeric value for federal tax rate.")
			
		while True:
			try:
				state_tax_rate = float(input("Enter state tax rate:  "))
				if state_tax_rate < 0:
					print("Please enter a valid rate.")
					continue
				break
			except ValueError:
				print("Invalid Input. Please enter a numeric value for state tax rate.")

		employee = Employee(name, pay_rate, gross_pay, federal_tax_rate, state_tax_rate)
		employee_map[name] = employee
		print(f"Employee added: {vars(employee)}")
	
	print("Payroll Summary:   ")
	for emp in employee_map.values():
		hours_worked = int(input(f"Enter hours worked for {emp.name}:  "))
		net_pay = emp.calculate_net_pay(hours_worked)
		print(f"{emp.name}, Net Pay:  {net_pay:.2f}")

if __name__ == "__main__":
	main()