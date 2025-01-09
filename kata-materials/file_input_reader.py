from submarine import Submarine

class FileInputReader:
    """
    A class to read commands from a file and apply them to a Submarine object.
    """

    def read_file(self, sub: Submarine, filename):
        """
        Reads a file containing commands and applies them to the given Submarine object.

        Args:
            sub (Submarine): The Submarine object to apply the commands to.
            filename (str): The name of the file containing the commands.
            verbose (bool, optional): If True, prints additional information during execution. Defaults to False.

        The file should contain commands in the format:
        <command> <units>
        Each line represents a command and the units to move the submarine.
        """

        with open(filename) as file:
            for line in file:
                [command, units_str] = line.rstrip().split(" ")
                units = int(units_str)

                sub.move(command, units)
