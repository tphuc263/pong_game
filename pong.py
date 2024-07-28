from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.x_cor = 10
        self.y_cor = 10


    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    #detect collision with top screen
    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_cor *= -1
        self.y_cor *= -1
