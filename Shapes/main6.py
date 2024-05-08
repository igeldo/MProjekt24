from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.oval import Oval


class Main:
    def test(self, **kwargs):
        print(f"test")
        print(f"   kwargs: {kwargs}")
        self.test2(**kwargs)

    def test2(self, a: float, b: float, c: float):
        print(f"test2")
        print(f"   a: {a}")
        print(f"   b: {b}")
        print(f"   c: {c}")


if __name__ == '__main__':
    main = Main()

    main.test(c=3, b=2, a=1)
