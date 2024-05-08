from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.circle import Circle
from graphics.shape.rectangle import Rectangle


class Oval(Rectangle, Circle):

    def __init__(self, width: float, height: float, **kwargs) -> None:
        super().__init__(width=width, height=height, radius=height / 2, **kwargs)

    def calculate_area(self) -> float:
        return Rectangle.calculate_area(self) + Circle.calculate_area(self)

    def plot(self, plot: Plot, color: str = 'red') -> None:
        Rectangle.plot(self, plot, color)
        plot.plot_circle(Point(self._p1.get_x(), self.get_center().get_y()), self._radius, color)
        plot.plot_circle(Point(self._p2.get_x(), self.get_center().get_y()), self._radius, color)

    def __str__(self) -> str:
        return f"Oval({self.get_center()},{self.get_width()},{self.get_height()})"
