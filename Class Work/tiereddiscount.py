total_spending = int(input('Enter The purchase your total spending:   '))
discount1 = 0.05
discount2 = 0.10
discount3 = 0.20
discount_price1 = total_spending * discount1
discount_price2 = total_spending * discount2
discount_price3 = total_spending * discount3
price_after_discount1 = total_spending - discount_price1
price_after_discount2 = total_spending - discount_price2
price_after_discount3 = total_spending - discount_price3

if total_spending >= 1000 and total_spending < 10000:
	print(f'Your discount price is {discount_price1:,.2f} and amount to be paid is {price_after_discount1:,.2f}')
elif total_spending >= 10000 and total_spending <= 50000:
	print(f'Your discount price is {discount_price2:,.2f} and amount to be paid is {aprice_after_discount2:,.2f}')
elif total_spending > 50000:
	print(f'Your discount price is {discount_price3:,.2f} and amount to be paid is {price_after_discount3:,.2f}')
else:
	print('Sorry no discount for you')