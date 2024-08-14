import unittest
from unittest.mock import MagicMock, patch
from src.langman.commands import add_, remove_, list_
from src.langman.manager import Manager
from src.langman.language import Language
from src.langman.program import Program

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.manager = MagicMock(spec=Manager)

    def test_add_language(self):
        add_(self.manager, "language", "Python")
        self.manager.add_item.assert_called_once_with("language", "Python")

    def test_add_program(self):
        add_(self.manager, "program", "MyProgram")
        self.manager.add_item.assert_called_once_with("program", "MyProgram")

    def test_remove_item(self):
        self.manager.get_item.return_value = Language(name="Python")
        remove_(self.manager, "Python")
        self.manager.remove_item.assert_called_once_with("Python")

    def test_remove_item_not_found(self):
        self.manager.get_item.return_value = None
        remove_(self.manager, "NonExistentItem")
        self.manager.remove_item.assert_not_called()

    def test_list_items(self):
        self.manager.list_items.return_value = [
            Language(name="Python"),
            Program(name="MyProgram", version="2.0")
        ]
        with patch('builtins.print') as mocked_print:
            list_(self.manager)
            mocked_print.assert_any_call('Python')
            mocked_print.assert_any_call('MyProgram')

if __name__ == "__main__":
    unittest.main()