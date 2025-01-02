import unittest

from file_input_reader import FileInputReader
from submarine import Submarine

class TestFileInputReader(unittest.TestCase):
    SHORT_INPUT_FILENAME = "short_input.txt"

    def test_read_simple_file(self):
        reader = FileInputReader()
        sub = Submarine()
        reader.read_file(sub, self.SHORT_INPUT_FILENAME)
        self.assertEqual(sub.depth, 10)
        self.assertEqual(sub.horizontal_position, 15)

if __name__ == "__main__":
    unittest.main()
