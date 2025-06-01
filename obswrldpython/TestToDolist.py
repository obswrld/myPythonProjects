import unittest
from to_dolist import to_dolist, create_console
from to_dolist import to_dolist, view_task
from to_dolist import to_dolist, view_mark_task_completed
from to_dolist import to_dolist, delete_task

class TestToDolist (unittest.TestCase):

	def test_set_up(self):
		global to_dolist
		to_dolist = []

	def test_create_console(self):
		create_console("Task 1")
		self.assertEqual(to_dolist, ["Task 1"])

	def test_view_task_empty(self):
		with self.assertLogs(level='INFO') as log:
			view_task()
			self.assertIn("No task available.", log.output)

	def test_view_task_non_empty(self):
		create_console("Task 1")
		create_console("Task 2")
		with self.assertLogs(level='INFO') as log:
			view_task()
			self.assertIn("1: Task 1", log.output)
			self.assertIn("2: Task 2", log.output)

	def test_mark_task_completed(self):
		create_console("Task 1")
		view_mark_task_completed(0)
		self.assertEqual(to_dolist, [])

	def test_delete_task(self):
		create_console("Task 1")
		delete_task(0)
		self.assertEqual(to_dolist, [])