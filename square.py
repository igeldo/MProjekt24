from point import Point
from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self,*,  a, **kwargs):
        super().__init__( a=a, b=a, **kwargs)
