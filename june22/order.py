import turtle
import random

screen = turtle.Screen()

bg_colors = ["lightblue", "lightgreen", "lightyellow", "pink", "lightgray"]
screen.bgcolor(random.choice(bg_colors))


class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


class Square(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def draw(self):
        turtle.color(self.color)
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        turtle.color(self.color)
        for i in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)


class Triangle(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def draw(self):
        turtle.color(self.color)
        for i in range(3):
            turtle.forward(self.size)
            turtle.right(120)

class Hexagon(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def draw(self):
        turtle.color(self.color)
        for i in range(6):
            turtle.forward(self.size)
            turtle.right(60)


class Octagon(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def draw(self):
        turtle.color(self.color)
        for i in range(8):
            turtle.forward(self.size)
            turtle.right(45)

def random_move():
    turtle.penup()
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.pendown()


shape_classes = [Square, Rectangle, Triangle, Hexagon, Octagon]

colors = ["red", "blue", "green", "purple", "orange", "black", "cyan"]

n = int(input("How many shapes do you want? "))

for i in range(n):
    shape_type = random.choice(shape_classes)
    color = random.choice(colors)

    random_move()

    if shape_type == Square:
        shape = Square(random.randint(30, 100), color)

    elif shape_type == Rectangle:
        shape = Rectangle(
            random.randint(40, 120),
            random.randint(30, 100),
            color
        )

    elif shape_type == Triangle:
        shape = Triangle(random.randint(40, 100), color)

    elif shape_type == Hexagon:
        shape = Hexagon(random.randint(30, 80), color)

    else:
        shape = Octagon(random.randint(30, 80), color)

    shape.draw()


turtle.done()