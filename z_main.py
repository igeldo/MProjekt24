from oval import  Oval
from circle import Circle
from point import Point
from rectangle import Rectangle
from square import Square
from triangle import Triangle


class Main:
    def run(self):
        print(f"MRO: {Oval.__mro__}")
        p = Point(1, 2)
        print("p: " + p.__str__())
        print("p: " + str(p))
        print(f"p: {p}")

        r = Rectangle(p=p, a=3, b=4)
        print(f"r: area {r.area()}")
        print(f"r: perimeter  {r.perimeter()}")

        s = Square (p=p,a=6)
        print(f"s: area  {s.area()}")
        print(f"s: perimeter  {s.perimeter()}")

        c = Circle(p=p,r=3)
        print(f"c: area {c.area()}")
        print(f"c: perimeter  {c.perimeter()}")

        t = Triangle(p=p, a=3, b=2)
        print(f"t: area {t.area()}")

        o = Oval(p=p, x=3)
        print(f"o: area {o.area()}")


if __name__ == '__main__':
    main = Main()
    main.run()
