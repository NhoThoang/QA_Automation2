# classmethod, staticmethod, property
class math:
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def add(x, y):
        return x + y
    # @staticmethod
    def subtract(self,  y):
        return self.value - y
print(math.add(2, 3))  # Output: 5
print(math(value=10).subtract(2))  # Output: 3
# @staticmethod not get instance (self) as first argument

class Dog:
    species = "Canine"
    fasd= "gádf"

    def __init__(self, name):
        self.name = name

    def speak(self):  # dùng self
        return f"My name is {self.name}"

    @classmethod
    def get_species(abbr):  # dùng cls
        return f"All dogs are {abbr.species}"
    @classmethod
    def get_fasd(abbr):  # dùng cls
        return f"All dogs are {abbr.species}"
print(Dog.get_species())  # Output: All dogs are Canine
# @classmethod not get instance (self) as first argument
print(Dog("Buddy").speak())  # Output: My name is Buddy
print(Dog.get_fasd())  # Output: fasd is gádf fasd

class math2:
    def __init__(self, value):
        self.value = value
    
    @property
    def add(self):
        def inner(y):
            return self.value + y
        return inner
    @property
    def subtract(self):
        return self.value - 2
print(math2(value=10).add(2))  # Output: 12
print(math2(value=10).subtract)  # Output: 8


from enum import Enum
class Direction(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

    FORWARD = "up"
    BACKWARD = "down"
    

    HORIZ_FORWARD = "left"
    HORIZ_BACKWARD = "right"

def move(direction: Direction):
    if direction in (Direction.UP, Direction.FORWARD):
        return "Moving upward"
    elif direction in (Direction.DOWN, Direction.BACKWARD):
        return "Moving downward"
    elif direction in (Direction.LEFT, Direction.HORIZ_FORWARD):
        return "Moving left"
    elif direction in (Direction.RIGHT, Direction.HORIZ_BACKWARD):
        return "Moving right"
    else:
        return "Unknown direction"
    

# Test
print(move(direction=Direction.UP))         # Moving upward
print(move(Direction.HORIZ_BACKWARD))  # Moving right


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction: Direction):
        if direction in (Direction.UP, Direction.FORWARD):
            self.y += 1
        elif direction in (Direction.DOWN, Direction.BACKWARD):
            self.y -= 1
        elif direction in (Direction.LEFT, Direction.HORIZ_FORWARD):
            self.x -= 1
        elif direction in (Direction.RIGHT, Direction.HORIZ_BACKWARD):
            self.x += 1

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"

# Test
pos = Position()
print(pos)  # Position(x=0, y=0)
pos.move(direction="up")
# pos.move(Direction.HORIZ_BACKWARD)
print(pos)  # Position(x=1, y=1)

# @cache_property
from functools import cached_property
class MyClass:
    @cached_property
    def result(self):
        print("Calculating...")
        return sum(range(1_000_000))

obj = MyClass()
print(obj.result)  # Output: Calculating... then the result
print(obj.result)  # Output: Result without recalculating
# @retry
from tenacity import retry
from tenacity import retry, wait_fixed, stop_after_attempt
import random

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def unstable_task():
    print("Thử kết nối...")
    if random.random() < 0.8:
        raise RuntimeError("Lỗi tạm thời!")
    print("Thành công!")

unstable_task()


from deprecated import deprecated

class MyLib:
    @deprecated(reason="Hàm này sẽ bị xoá ở phiên bản 2.0. Dùng new_method() thay thế.")
    def old_method(self):
        print("Hàm cũ đang chạy.")

    def new_method(self):
        print("Hàm mới đang chạy.")
print(MyLib().old_method())  # Cảnh báo: Hàm này sẽ bị xoá ở phiên bản 2.0. Dùng new_method() thay thế.
print(MyLib().new_method())  # Hàm mới đang chạy.


from contextlib import contextmanager

@contextmanager
def open_file(path):
    f = open(path, 'r')
    try:
        yield f  # Mã gọi `with` sẽ dùng giá trị này
    finally:
        f.close()

# Dùng như context manager
with open_file('hello.txt') as f:
    data = f.read()
    print(data)
class OpenFile:
    def __init__(self, path):
        self.f = open(path, 'r')

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
@contextmanager
def catch_exception():
    print("Bắt đầu...")
    try:
        yield
    except Exception as e:
        print("Lỗi được bắt:", e)
    finally:
        print("Kết thúc")

with catch_exception():
    print("Thử chia...")
    1 / 0  # Sẽ được bắt
