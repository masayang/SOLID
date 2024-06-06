'''
OCP: Open/Closed Principle (開放閉鎖の原則)
'''


class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle and the radius is {self.radius}")


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        print(f"Drawing a square and the side length is {self.side_length}")


if __name__ == "__main__":
    circle = Circle(5)
    circle.draw()

    square = Square(10)
    square.draw()