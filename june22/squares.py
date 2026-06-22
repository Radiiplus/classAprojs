import turtle
import random


class Square:
    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

        turtle.color(self.color)

        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)


# Main program
n = int(input("Enter number of squares: "))

colors = ["red", "blue", "green", "purple", "orange", "black", "pink"]

for i in range(n):
    size = random.randint(20, 100)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(colors)

    square = Square(size, color, x, y)
    square.draw()

turtle.done()