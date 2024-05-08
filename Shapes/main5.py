from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.oval import Oval


class Main:
    def test(self, **kwargs):
        print(f"test")
        print(f"   kwargs: {kwargs}")
        print(f"   a: {kwargs['a']}")
        print(f"   b: {kwargs['b']}")
        print(f"   c: {kwargs['c']}")


if __name__ == '__main__':
    main = Main()

    main.test(c=3, b=2, a=1)
