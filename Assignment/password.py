password = input('Please Enter Your Password:   ')
password_count = len(password)
if password_count < 8:
	print('Password too weak')
if password_count == 8:
	print('Password is weak')
if password_count > 8 and password_count <= 16:
	print('password is Strong')
if password_count > 16:
	print('Password very Strong')

