to_dolist = []
def create_console(tasks):
	to_do = [task]
	to_dolist.append(to_do)

def view_task():
	for task in to_dolist:
		print(to_dolist)

def veiw_mark_task_completed():
	for task in to_dolist:
		if task == choose:
			to_dolist[to_do]
	return to_dolist 

def delete_task():
	for task in to_dolist:
		if task == choose:
			to_dolist[0].remove
	return to_dolist 

menu_options = True
while menu_options:
	message_menu ="""
Welcome to the To Do list Menu

What List would you like to do today?

=> Add a Task
=> View all Tasks
=> Mark a task as complete
=> Delete a task
=> Exit
"""
print(message_menu)
user_input = int(input('Enter a number for your choice.'))

match(user_input):
	case 1:
		add = """
		Welcome to Add task menu
		=> Add task
		=> Go back to Menu
		"""
		print(add)
		user_input1 = int(input('Enter Your task'))
		create_console(user_input1)
					
		add_result = """
		Task has just been added.
		"""
		print(add_result)

	case 2: 
		view = """
		Welcome to Viewing all task menu
		Here are your list of taks
		=> press 0 to Go back 
		"""
		print(view)
		view_task()
		user_input2 = int(input('Enter or press 0 to o back'))

		match(user_input2):
				case 0: 
						massage_task = """
						Goodbye
						"""

						print(message_task)

				case _: 
						print("Invalid Number")
	case 3: 

		message = """
		Option menu to mark task as complete

		=> Would you like to mark any the task
		=> press 1 to mark your pefered and complete task
		=> press 0 to go back 
		"""
		
		print(message)
		view_task()
		user_input3 = int(input('Enter the task to mark'))

		match(user_input3):
		case 1: 
			choose = int(input(Enter the task to be marked))
			view_mark_task_completed()					
		case 0: 
			message_taks = """
			Bye
			"""
			print(message_task)
		case_:
			print("Invalid Input")

	case 4:

		message = """
		Option Menu to delete task

		=> Would you like to delete any of the task
		=> press 1 to delete the prefered task 
		=> press 0 to go back
		"""

		print(message)
		view_task()
		user_input4 = int(input(Enter the task to delete))
				

			
		
			
			

					 
		