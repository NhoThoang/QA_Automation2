import enum
from typing import Optional, Tuple, Union

SCROLL_STEPS = 55
HTTP_TIMEOUT = 300

class Direction(str, enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

    # 垂直操作
    FORWARD = "up"
    BACKWARD = "down"

    # 水平操作
    HORIZ_FORWARD = "left"
    HORIZ_BACKWARD = "right"
class cached_property:
    def __init__(self, func):
        self.func = func
        self.attrname = None
        self.__doc__ = func.__doc__
class Device(object):
    def __init__(self, d):
        self._d = d
    @cached_property
    def swipe_ext(self) -> SwipeExt:
        return SwipeExt(self)
    
class SwipeExt(object):
    def __init__(self, d):
        """
        Args：
            d (uiautomator2.Device)
        """
        self._d = d

    def __call__(self,
                 direction: Union[Direction, str],
                 scale: float = 0.9,
                 box: Optional[Tuple[int, int, int, int]] = None,
                 **kwargs):
        pass

from functools import cached_property
from ._proto import Direction


from functools import cached_property

class MyClass:
    @cached_property
    def result(self):
        print("Đang tính toán...")
        return sum(range(1_000_000))

obj = MyClass()
print(obj.result)  # In: Đang tính toán... rồi kết quả
print(obj.result)  # Không tính lại, chỉ in kết quả


import enum

class Direction(enum.Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
print(Direction.UP)         # Direction.UP
print(Direction.UP.value)   # "up"
