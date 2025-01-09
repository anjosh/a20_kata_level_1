from file_input_reader import FileInputReader
from submarine import Submarine
import argparse

"""
A script to calculate the product of a submarine's depth and horizontal position 
after executing movement commands from an input file.
"""

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    help="Output the submarine's depth and horizontal position after following each command",
                    action='store_true')
args = parser.parse_args()

sub = Submarine()
file_input_reader = FileInputReader()

file_name = "input.txt"
file_input_reader.read_file(sub, file_name, args.verbose)

print("----------------------------")
print(f"Product of Submarine Depth and Horizontal Position: {sub.depth * sub.horizontal_position}")
print("----------------------------")
