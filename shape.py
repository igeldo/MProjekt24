from abc import abstractmethod, ABC

from point import Point


class Shape(ABC):

    def __init__(self, *, p: Point):
        self._p = p

#    @abstractmethod
 #   def area(self):
 #       pass

#   @abstractmethod
#    def perimeter(self):
#       pass