from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.oval import Oval


class Main:
    def run(self):
        plot = Plot()

        oval = Oval(center = Point(8, 20), width=12, height=4)
        oval.plot(plot, 'mediumvioletred')
        print(f"{oval} has area: {oval.calculate_area()}")

        plot.show()


if __name__ == '__main__':
    main = Main()
    main.run()
