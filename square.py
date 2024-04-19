from point import Point
from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, p:Point,  a):
        super().__init__( p, a, a)
