
import enum

class Direction(enum.Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
print(Direction.UP)         # Direction.UP
print(Direction.UP.value)   # "up"
print(Direction.DOWN.name)       # Direction.DOWN
