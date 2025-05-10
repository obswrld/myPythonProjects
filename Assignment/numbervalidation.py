number = int(input("Enter number here:  "))
counter = int(0)
while number != 1 and number != 2:
	number = int(input("Enter number again:   "))
	counter = counter + 1
print(f"You failed the guess {counter} times")
	