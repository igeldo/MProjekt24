from point import Point
from shape import Shape


class Rectangle(Shape):

    def __init__(self, p:Point, a, b):
        super().__init__(p)
        self._width = a
        self._length = b

    def getWidth(self):
        return self._width

    def getLength(self):
        return self._length

    def area(self):
        print(f"rectangle {self._width}")
        return self._width * self._length

    def perimeter(self):
        return 2 * (self._width + self._length)
