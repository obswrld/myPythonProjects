import to_do_list
from to_do import to_dolist, create_console


class TestCube(TestCase):
		def test_that_create_console(self):
			create_console("Get the main work done", "Go home", )
			weself.assertEqual(2, len,(accounts))