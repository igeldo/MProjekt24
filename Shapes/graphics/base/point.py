from __future__ import annotations

from graphics.base.coordinate2d import Coordinate2D
from graphics.base.util import check_type
from graphics.base.vector import Vector


class Point(Coordinate2D):

    def __str__(self) -> str:
        return f"Point({self._x},{self._y})"

    def __add__(self, other: Vector) -> Point:
        check_type(other, Vector, 'other')
        return Point(self.get_x() + other.get_x(), self.get_y() + other.get_y())
