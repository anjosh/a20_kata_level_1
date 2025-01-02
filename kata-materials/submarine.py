from command import Command

class Submarine:
    def __init__(self, depth:int=0, horizontal_position:int=0):
        self.depth = depth
        self.horizontal_position = horizontal_position

    def __str__(self) -> str:
        return f"Depth: {self.depth}\tHorizontal Position: {self.horizontal_position}"


    def move(self, command:str, units:int, verbose:bool=False):
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
