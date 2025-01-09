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
parser.add_argument("--file_name",
                    help="Name of file containing the input for the submarine",
                    default="input.txt")
args = parser.parse_args()

sub = Submarine(args.verbose)
file_input_reader = FileInputReader()

file_input_reader.read_file(sub, args.file_name)

print("----------------------------")
print(f"Product of Submarine Depth and Horizontal Position: {sub.depth * sub.horizontal_position}")
print("----------------------------")
