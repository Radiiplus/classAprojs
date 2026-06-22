import turtle

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def draw(self):
        turtle.color(self.color)
        turtle.circle(self.radius)

class Square:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        turtle.color(self.color)
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)

class Octagon:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        turtle.color(self.color)
        for i in range(8):
            turtle.forward(self.size)
            turtle.right(45)


# Main program
print("1. Circle")
print("2. Square")
print("3. Octagon")

choice = input("Choose shape: ")
color = input("Enter color: ")

if choice == "1":
    r = int(input("Enter radius: "))
    shape = Circle(r, color)

elif choice == "2":
    s = int(input("Enter size: "))
    shape = Square(s, color)

elif choice == "3":
    s = int(input("Enter size: "))
    shape = Octagon(s, color)

else:
    print("Invalid choice")
    exit()

shape.draw()
turtle.done()