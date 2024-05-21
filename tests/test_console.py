import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(), "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertNotEqual(f.getvalue(), "")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertNotEqual(f.getvalue(), "")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("update BaseModel {} name 'NewName'".format(obj_id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            self.assertEqual(f.getvalue().strip(), "2")

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel invalid_id name 'NewName'")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_invalid_attribute(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("update BaseModel {} invalid_attribute 'NewValue'".format(obj_id))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    # Add similar test methods for other classes and methods

if __name__ == "__main__":
    unittest.main()

