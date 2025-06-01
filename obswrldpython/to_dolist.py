to_dolist = []

def create_console(task):
	to_dolist.append(task)

def view_task():
	if not to_dolist:
		print("No task available")
	else:
		for index, task in enumerate(to_dolist):
			print(f"{index + 1}: {task}") 

def view_mark_task_completed(task_index):
	if 0 <= task_index < len(to_dolist):
		print(f"Task '{to_dolist[task_index]}' marked as completed.")
		del to_dolist[task_index]
	else:
		print("Invalid task Number.")

def delete_task(task_index):
	if 0 <= task_index < len(to_dolist):
		removed_task = to_dolist.pop(task_index)
		print(f"Task '{removed_task}' deleted.")
	else:
		print("Invalid task number.")

menu_options = True
while menu_options:
	message_menu = """
Welcome to the To Do List Menu

What would you like to do today?

1 => Add a task 
2 => View all task
3 => Mark a task as completed 
4 => Delete a task
0 => Exit
"""
	print(message_menu)
	try:
		user_input = int(input("Enter a Number for your choice."))
		match user_input:
			case 1:
				user_input1 = input("Enter Your task:  ")
				create_console(user_input1)
				print("Task has just been added.")
			case 2: 
				print("Here are your list of tasks: ")
				view_task()
				input("Press Enter to go back....")
			case 3: 
				view_task()
				user_input3 = int(input("Enter a task number to mark as complete:   "))
				view_mark_task_completed(user_input3)
			case 4: 
				view_task()
				user_input4 = int(input("Enter the task to delete:   "))
				delete_task(user_input4)
			case 0: 
				menu_options = False
				print("Exiting.....")
			case _:
				print("Invalid Input. Please try again.")

	except ValueError:
		print("Please enter a valid number.")