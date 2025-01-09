from enum import Enum

class Command(Enum):
    """
    An Enum class that stores the types of expected commands.
    """

    UP = 1
    DOWN = 2
    FORWARD = 3
