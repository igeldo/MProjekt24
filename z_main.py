
from circle import Circle
from point import Point
from rectangle import Rectangle
from square import Square



class Main:
    def run(self):
        p = Point(1, 2)
        print("p: " + p.__str__())
        print("p: " + str(p))
        print(f"p: {p}")

        r = Rectangle(p, 3, 4)
        print(f"r: area {r.area()}")
        print(f"r: perimeter  {r.perimeter()}")

        s = Square (p, 6)
        print(f"s: area  {s.area()}")
        print(f"s: perimeter  {s.perimeter()}")

        c = Circle(p, 3)
        print(f"c: area {c.area()}")
        print(f"c: perimeter  {c.perimeter()}")



if __name__ == '__main__':
    main = Main()
    main.run()
