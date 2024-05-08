from math import pi

from graphics.base.util import check_float_positive
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Circle(Shape):

    def __init__(self, radius: float, **kwargs) -> None:
        print(f"Circle, radius: {radius}")
        print(f"   kwargs: {kwargs}")
        super().__init__(**kwargs)
        self._radius = check_float_positive(radius, 'radius')

    def get_radius(self) -> float:
        return self._radius

    def calculate_area(self) -> float:
        return pi * self._radius ** 2

    def plot(self, plot: Plot, color: str = 'red') -> None:
        plot.plot_circle(self.get_center(), self.get_radius(), color)

    def __str__(self) -> str:
        return f"Circle({self.get_center()},{self.get_radius()})"
