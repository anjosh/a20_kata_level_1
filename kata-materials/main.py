from file_input_reader import FileInputReader
from submarine import Submarine

sub = Submarine()
file_input_reader = FileInputReader()

file_name = "input.txt"
file_input_reader.read_file(sub, file_name, verbose=True)

print("----------------------------")
print(f"Product of Submarine Depth and Horizontal Position: {sub.depth * sub.horizontal_position}")
print("----------------------------")
