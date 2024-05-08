from graphics.shape.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, width: float, **kwargs) -> None:
        super().__init__(width=width, height=width, **kwargs)

    def __str__(self) -> str:
        return f"Square({self.get_center()},{self.get_width()})"
