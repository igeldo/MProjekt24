
from circle import Circle
from square import Square


class Oval(Square,Circle):

    def __init__(self, *, x, **kwargs):
        super().__init__(a=x,r=x/2, **kwargs)

    def area(self):
        return Circle.area(self) + Square.area(self)
