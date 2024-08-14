import unittest
from src.langman.program import Program

class TestProgram(unittest.TestCase):
    def test_program_creation(self):
        program = Program(name="MyProgram")
        self.assertEqual(program.name, "MyProgram")
        self.assertEqual(program.version, "1.0")

    def test_program_creation_with_version(self):
        program = Program(name="MyProgram", version="2.0")
        self.assertEqual(program.version, "2.0")

    def test_program_to_dict(self):
        program = Program(name="MyProgram", version="2.0")
        program_dict = program.to_dict()
        expected_dict = {
            "name": "MyProgram",
            "version": "2.0"
        }
        self.assertEqual(program_dict, expected_dict)

    def test_program_from_dict(self):
        program_data = {
            "name": "MyProgram",
            "version": "2.0"
        }
        program = Program.from_dict(program_data)
        self.assertEqual(program.name, "MyProgram")
        self.assertEqual(program.version, "2.0")

if __name__ == "__main__":
    unittest.main()