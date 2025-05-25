def main():
	while True:
			main_menu()
			num = int(input('Please Select an option:  '))

			if num == 0:
				print('Exiting. . . . . .')
				break
			if num < 1 or num > 13:
				print('Invalid Option. Please select a number between 1 and 13 or enter 0 to exit.')
				continue

			if num == 1:
				phonebook()
			if num == 2:
				message()
			elif num == 3:
				print('Chat')
				goback()
			elif num == 4:
				call_register()
			elif num == 5:
				tones()
			elif num == 6:
				settings()
			elif num == 7:
				print('Call Divert')
				goback()
			elif num == 8:
				print('Games')
				goback()
			elif num == 9:
				print('Calculator')
				goback()
			elif num == 10:
				print('Reminders')
				goback()
			elif num == 11:
				clock()
			elif num == 12:
				print('Profiles')
				goback()
			elif num == 13:
				print('SIM service')
				goback()
def main_menu():
	menu = """
	Welcome!
	Menu Functions:
	1=> Phonebook
	2=> Message
	3=> Chat
	4=> Call Register
	5=> Tones
	6=> Settings
	7=> Call Divert
	8=> Games
	9=> Calculators
	10=> Reminders
	11=> Clock
	12=> Profiles
	13=> Sim service 
	0=> Exit
	"""
	print(menu)





def phonebook():
	while True:
		phonebook_menu()
		num1 = int(input('Please Select An Option:  '))

		if num1 == 0:
			break
	
		if num1 < 1 or num1 > 10:
			print('Please Enter A Valid Number between 1 and 10.')
			continue

		if num1 == 1:
			print('Search.')
			goback()
		elif num1 == 2:
			print('Search Nos.')
			goback()
		elif num1 == 3:
			print('Add name.')
			goback()
		elif num1 == 4:
			print('Erase.')
			goback()
		elif num1 == 5:
			print('Edit.')
			goback()
		elif num1 == 6:
			print('Assign Tone.')
			goback()
		elif num1 == 7:
			print("Send b'card.")
			goback()
		elif num1 == 8:
			options()
		elif num1 == 9:
			print('Speed Dials')
			goback()
		elif num1 == 10:
			print('Voice Tags')
			goback()
def phonebook_menu():
	phone = """
	Phonebook Menu:
	1 => Search
	2 => Service Nos.
	3 => Add name 
	4 => Erase 
	5 => Edit 
	6=> Asign Tone
	7=> Send b'card  
	8=> Options
	9=> Speed Dials 
	10=> Voice Tags 
	0=> Back to menu
	"""
	print(phone)





def options():
	while True:
		options_menu()
		num2 = int(input('Please Select an Option:  '))
		
		if num2 == 0:
			break

		if num2 < 1 or num2 > 2:
			print('Invalid Option. Please Select A Number between 1 and 2.')
			continue
		
		if num2 == 1: 
			print('Type of View')
			goback()

		elif num2 == 2:
			print('Memory Status')
			goback()
def options_menu():
	options  = """
	options menu:
	1 => Type of View
	2 => Memory Status 
	0 => Back to Phonebook
	"""
	print(options)





def message():
	while True:
		message_menu()
		num3 = int(input('Please Select an Option:  '))
	
		if num3 == 0:
			break

		if num3 < 1 or num3 > 10:
			print('Invalid Number. Please Select a Number between 1 and 10.')
			contnue

		if num3 == 1:
			print('Write Message.')
			goback()
		if num3 == 2: 
			print('Inbox')
			goback()
		if num3 == 3:
			print('Outbox')
			goback()		
		if num3 == 4:
			print('Pictures Messages')
			goback()
		if num3 == 5: 
			print('Templates')
			goback()
		if num3 == 6:
			print('Smileys')
			goback()
		if num3 == 7:
			message_settings()
		if num3 == 8: 
			print('Info Service')
			goback()
		if num3 == 9:
			print('Voice Mailbox Number')
			goback()
		if num3 == 10:
			print('Service Command Editor.')
			goback()
def message_menu():
	message = """
	Message
	1 => Write message 
	2 => Inbox 
	3 => Outbox
	4 => Pictures message 
	5 => Templates 
	6 => Smileys
	7 => Message settings 
	8 => Voice mailbox number
	9 => Voice mailbox number
	10 => Service command editor 
	0 => Back to menu
	"""
	print(message)





def message_settings():
	while True:
		message_settings_menu()
		num4 = int(input('Please Select an Option:  '))

		if num4 == 0:
			break
		
		if num4 < 1 or num4 > 2:
			print('Invalid Number. Please Select a Number between 1 and 2.')
			continue

		if num4 == 1:
			set_message()
		elif num4 == 2: 
			common_settings()
def message_settings_menu():
	message_setting = """
	Message settings 
	1 => Set 1
	2 => Common
	0 => Back to Message 
	"""
	print(message_setting)





def set_message():
	while True:
		set_menu()
		num5 = int(input('Please Seleact an Option.'))

		if num5 == 0:
			break
		
		if num5 < 1 or num5 > 3:
			print('Invalid Number. Please Number between 1 and 3.')
			continue

		if num5 == 1:
			print('Message Center Number.')
			goback()

		if num5 == 2:
			print('Message Sent as')
			goback

		if num5 == 3:
			print('Message Validity')
			goback()
def set_menu():
	set_menu = """
	Set 1
	1 => Message center number
	2 => Message sent as 
	3 => Message valididty
	0 => Back to Message Settings
	"""
	print(set_menu)





def common_settings():
	while True:
		common_menu()
		num6 = int(input('Please Select an Option:   '))

		if num6 == 0:
			break
		
		if num6 < 1 or num6 > 3:
			print('Invalid Number. Please select between 1 and 3.')
			continue

		if num6 == 1:
			print('Delievery Reports.')
			goback()
		if num6 == 2:
			print('Reply Via Center')
			goback()
		if num6 == 3: 
			print('Character Support')
			goback()
def common_menu():
	common = """
	Common
	1 => Delivery Reports 
	2 => Reply Via Same Center 
	3 => Character Support
	0 => Back to Message Settings 
	"""
	print(common)





def call_register():
	while True:
		call_register_menu()
		num7 = int(input('Please Select an Option:  '))

		if num7 == 0:
			break
		if num7 < 1 or num7 > 8:
			print('Invalid Number. Please Select a Number between 1 and 8. ')
		if num7 == 1:
			print('Missed calls')
			goback()
		if num7 == 2:
			print('Recieved calls')
			goback()
		if num7 == 3:
			print('Dialled numbers')
			goback()
		if num7 == 4:
			print('Erase recent call lists')
			goback()
		if num7 == 5:
			show_call_duration()
		if num7 == 6:
			show_call_cost()
		if num7 == 7:
			call_cost_settings()
		if num7 == 8:
			print('Prepaid credit')
			goback()
def call_register_menu():
	call = """
	Call register
	1 => Missed calls 
	2 => Received calls 
	3 => Dialled numbers
	4 => Erase recent call lists 
	5 => Show call duration
	6 => Show call cost
	7 => Call cost setings
	8 => Prepaid credit 
	0 => Back to menu
	"""
	print(call)	





def show_call_duration():
	while True:
		show_call_duration_menu()
		num8 = int(input('Please Select an Option:  '))

		if num8 == 0:
			break
		if num8 < 1 or num8 > 5:
			print('Invalid Number. Please Select a Number between 1 and 5.')
			continue
		
		if num8 == 1:
			print('Last call duration.')
			goback()
		if num8 == 2:
			print("All calls' duration")
			goback()
		if num8 == 3:
			print("Recieved call's duration")
			goback()
		if num8 == 4:
			print("Dialled calls' duration")
			goback()
		if num8 == 5:
			print('Clear timers')
def show_call_duration_menu():
		call_duration = """
		Show call duration
		1 => Last call duration 
		2 => All calls' duration
		3 => Recieved calls' duration
		4 => Dialled calls' duration
		5 => clear timers 
		0 => Back to call register 
		"""
		print(call_duration)





def show_all_cost():
	while True:
		show_all_cost_menu()
		num9 = int(input('Please Select an Option:  '))
		
		if num9 == 0:
			break
	
		if num9 < 1 or num9 > 3:
			print('Invalid Number. Please Select a Number between 1 and 3.')
			continue
	
		if num9 == 1:
			print('Last call cost')
			goback()
		if num9 == 2:
			print("All calls' cost")
			goback()
		if num9 == 3:
			print('Clear counters')
def show_all_cost_menu():
	all_cost = """
	Show call costs
	1 => Last call costs
	2 => All calls' cost
	3 => Clear counters
	0 => Back to call register
	"""
	print(all_cost)





def call_cost_settings():
	while True:
		call_cost_settings_menu()
		num10 = int(input('Please Select an Option:  '))
		
		if num10 == 0:
			break

		if num10 < 1 or num10 > 2:
			print('Invalid Number. Please Select a Number between 1 and 2')
			continue

		if num10 == 1:
			print('Call cost limit')
			goback()
		if num10 == 2:
			print('Show cost in')
			goback()
def call_cost_settings_menu():
	cost_settings = """
	Call cost settings
	1 => Call cost limit
	2 => Show costs in
	0 => Back to call register 
	"""
	print(cost_settings)





def tones():
	while True:
		tones_menu()
		num11 = int(input('Please Select an Option:  '))
		
		if num11 == 0:
			break
	
		if num11 < 1 or num11 > 9:
			print('Invalid Number. Please Select a Number between 1 and 9.')
			continue

		if num11 == 1:
			print('Ringing tone')
			goback()
		if num11 == 2:
			print('Ringing volume')
			goback()
		if num11 == 3:
			print('Incoming call alert')
			goback()
		if num11 == 4:
			print('Composer')
			goback()
		if num11 == 5:
			print('Message alert tone')
			goback()
		if num11 == 6:
			print('Keypad tones')
			goback()
		if num11 == 7:
			print('Warning and game tones')
			goback()
		if num11 == 8:
			print('Vibrating alert')
			goback()
		if num11 == 9:
			print('Screen saver')
			goback()
def tones_menu():
	tone = """
	Tones
	1 => Ringing tone
	2 => Ringing volume
	3 => Incoming call alert
	4 => Composer 
	5 => Message alert tone
	6 => Keypad tones
	7 => Warning and game tones 
	8 => Vibrating alert
	9 => Screen saver 
	0 => Back to menu
	"""
	print(tone)





def settings():
	while True:
		settings_menu()
		num13 = int(input('Please Select an Option:   '))
		
		if num13 == 0:
			break
	
		if num13 < 1 or num13 > 4:
			print('Invalid Number. Please Select a Number between 1 and 4.')
			continue

		if num13 == 1:
			calls_settings()
		if num13 == 2:
			phones_settings()
		if num13 == 3:
			security_settings()
		if num13 == 4:
			print('Restore factory settings')
			goback()
def settings_menu():
	set_menu = """
	Settings
	1 => Call settings
	2 => Phone settings
	3 => Security settings
	4 => Restore factory settings
	0 => Back to menu
	"""
	print(set_menu)





def calls_settings():
	while True:
		calls_settings_menu()
		num14 = int(input('Please Select an Option:   '))
	
		if num14 == 0:
			break
	
		if num14 < 1 or num14 > 6:
			print('Invalid Number. Please Select a Number between 1 and 6.')
			continue

		if num14 == 1:
			print('Automatic redial')
			goback()
		if num14 == 2:
			print('Speed dialing')
			goback()
		if num14 == 3:
			print('Call waiting options')
			goback()
		if num14 == 4:
			print('Own number sending')
			goback()
		if num14 == 5:
			print('Phone line in use')
			goback()
		if num14 == 6:
			print('Automatice answer')
			goback()
def calls_settings_menu():
	call_set_menu = """
	Call Settings
	1 => Automatic redial
	2 => Speed dialing
	3 => Call waiting options
	4 => Own number sending
	5 => Phone line use 
	6 => Automatic answer
	0 => Back to settings
	"""
	print(call_set_menu)





def phones_settings():
	while True:
		phones_settings_menu()
		num15 = int(input('Please Select an Option:   '))
	
		if num15 == 0:
			break
	
		if num15 < 1 or num15 > 6:
			print('Invalid Number. Please Select a Number between 1 and 6.')
			continue

		if num15 == 1:
			print('Language')
			goback()
		if num15 == 2:
			print('Cell info display')
			goback()
		if num15 == 3:
			print('Welcome note')
			goback()
		if num15 == 4:
			print('Network selection')
			goback()
		if num15 == 5:
			print('Lights')
			goback()
		if num15 == 6:
			print('Confirm SIM service actions')
			goback()
def phones_settings_menu():
	phone_set_menu = """
	Phone Settings
	1 => Language
	2 => Cell info display
	3 => Welcome note
	4 => Network selection
	5 => Lights
	6 => Confirm SIM service actions
	0 => Back to settings
	"""
	print(phone_set_menu)





def security_settings():
	while True:
		security_settings_menu()
		num16 = int(input('Please Select an Option:   '))
	
		if num16 == 0:
			break
	
		if num16 < 1 or num16 > 6:
			print('Invalid Number. Please Select a Number between 1 and 6.')
			continue

		if num16 == 1:
			print('PIN code request')
			goback()
		if num16 == 2:
			print('Call barring service')
			goback()
		if num16 == 3:
			print('Fixed dialling')
			goback()
		if num16 == 4:
			print('Closed user group')
			goback()
		if num16 == 5:
			print('Phone security')
			goback()
		if num16 == 6:
			print('Change access codes')
			goback()
def security_settings_menu():
	phone_set_menu = """
	Security Settings
	1 => PIN code request
	2 => Call barring service
	3 => Fixed dialling
	4 => Closed user group
	5 => Phone security
	6 => Change access codes
	0 => Back to settings
	"""
	print(phone_set_menu)





def clock():
	while True:
		clock_menu()
		num12 = int(input('Please Select an Option:   '))
		
		if num12 == 0:
			break;
	
		if num12 < 1 or num12 > 6:
			print('Invalid Number. Please Select a number between 1 and 6.')
			continue

		if num12 == 1:
			print('Alarm clock')
			goback()
		if num12 == 2:
			print('Clock settings')
			goback()
		if num12 == 3:
			print('Date setting')
			goback()
		if num12 == 4:
			print('Stopwatch')
			goback()
		if num12 == 5: 
			print('Countdown timer')
			goback()
		if num12 == 6:
			print('Auto update of date and time')
			goback()
def clock_menu():
	clocks = """
	Clock	
	1 => Alarm clock
	2 => Clock setting	
	3 => Date setting	
	4 => Stopwatch
	5 => Countdown timer 
	6 => Auto update of date and time
	0 => Back to menu
	"""
	print(clocks)





def goback():
	while input("Press 0 to go back:  ") != '0':
		print('Invalid Number. Press 0 to go back.')





if __name__ == "__main__":
    main()
