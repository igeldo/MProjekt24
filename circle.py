from math import pi

from point import Point
from shape import Shape

class Circle(Shape):

    def __init__(self, *, r, **kwargs):
        super().__init__(**kwargs)
        self._radius = r

    def getradius(self):
        return self._radius

    def area(self):
        print(f"circle {self._radius}")
        return pi * self._radius * self._radius

    def perimeter(self):
        return 2 * pi * self._radius