import to_do_list
from to_do import to_dolist, create_console
from to_do import to_dolist, view_task


class TestCube(TestCase):
		def test_that_create_console(self):
			create_console("David", "Go home")
			actual("David", "Go home")
			expected("David", "Go home")

		def test_that_view_task(self):
			view_task("")
			