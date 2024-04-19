from point import Point
from shape import Shape


class Triangle(Shape):

    def __init__(self, *, a, b, **kwargs):
        super().__init__( **kwargs)
        self._base = a
        self._hight = b

    def getBase(self):
        return self._base

    def getHight(self):
        return self._hight

    def area(self):
        return 0,5 * self._base * self._hight
