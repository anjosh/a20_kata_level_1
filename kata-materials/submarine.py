from command import Command

class Submarine:
    """
    Represents a submarine with depth and horizontal position attributes.
    Provides methods to move the submarine based on commands.

    Attributes:
        depth (int): The current depth of the submarine.
        horizontal_position (int): The current horizontal position of the submarine.
    """

    def __init__(self, depth: int = 0, horizontal_position: int = 0):
        """
        Initializes the Submarine instance with optional starting depth and horizontal position.

        Args:
            depth (int): Initial depth of the submarine. Defaults to 0.
            horizontal_position (int): Initial horizontal position of the submarine. Defaults to 0.
        """
        self.depth = depth
        self.horizontal_position = horizontal_position

    def __str__(self) -> str:
        """
        Returns a string representation of the submarine's current state.

        Returns:
            str: A formatted string displaying the submarine's depth and horizontal position.
        """
        return f"Depth: {self.depth}\tHorizontal Position: {self.horizontal_position}"

    def move(self, command: str, units: int, verbose: bool = False):
        """
        Moves the submarine based on the given command and number of units.

        Args:
            command (str): The direction to move ('UP', 'DOWN', 'FORWARD').
            units (int): The number of units to move in the given direction.
            verbose (bool): If True, prints the command and updated state. Defaults to False.

        Raises:
            ValueError: If the command is not recognized.
        """
        match command.upper():
            case Command.UP.name:
                self.depth -= units
            case Command.DOWN.name:
                self.depth += units
            case Command.FORWARD.name:
                self.horizontal_position += units
            case _:
                raise ValueError(f"Unrecognized Command. Command: {command}.")

        if verbose:
            print(f"{command}\t{units}\t{self}")
