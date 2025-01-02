from submarine import Submarine

class FileInputReader:
    def read_file(self, sub:Submarine, filename, verbose=False):
        with open(filename) as file:
            for line in file:
                [command, units_str] = line.rstrip().split(" ")
                units = int(units_str)

                sub.move(command, units, verbose)
