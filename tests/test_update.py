import unittest
from unittest.mock import patch, MagicMock
from src.langman.update import update
from pathlib import Path

class TestUpdateFunction(unittest.TestCase):
    @patch('subprocess.run')
    @patch('os.chdir')
    @patch('pathlib.Path.exists')
    def test_update_with_no_venv(self, mock_exists, mock_chdir, mock_run):
        mock_exists.return_value = False

        with patch('builtins.print') as mocked_print:
            update()
            mocked_print.assert_any_call("Virtual environment not found. Please set up the venv.")
            mock_run.assert_not_called()
            mock_chdir.assert_not_called()

    @patch('subprocess.run')
    @patch('os.chdir')
    @patch('pathlib.Path.exists')
    def test_update_already_up_to_date(self, mock_exists, mock_chdir, mock_run):
        mock_exists.return_value = True

        mock_run.return_value.stdout = "Already up to date.\n"

        with patch('builtins.print') as mocked_print:
            update()
            mock_chdir.assert_called_once()
            mock_run.assert_called_once_with(["git", "pull"], check=True, text=True, capture_output=True)
            mocked_print.assert_any_call("Already up to date. No changes were made.")

    @patch('subprocess.run')
    @patch('os.chdir')
    @patch('pathlib.Path.exists')
    def test_update_with_changes(self, mock_exists, mock_chdir, mock_run):
        mock_exists.return_value = True

        mock_run.return_value.stdout = "Updating somehash..otherhash\n"

        with patch('builtins.print') as mocked_print:
            update()
            mock_chdir.assert_called_once()
            self.assertEqual(mock_run.call_count, 2)  # One for git pull, one for pip install
            mocked_print.assert_any_call("Updates were pulled successfully!")
            mocked_print.assert_any_call("Package reinstalled successfully.")

if __name__ == "__main__":
    unittest.main()