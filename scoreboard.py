from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.write_score()
    def right_point(self):
        self.right_score += 1
        self.write_score()

    def game_over(self):
        if (self.left_score >= 5):
            self.goto(0,0)
            self.write("The left_player is the Winner ", align=ALIGNMENT, font=("Courier", 30, "normal"))
        if (self.right_score >= 5):
            self.goto(0, 0)
            self.write("The right_player is the Winner ", align=ALIGNMENT, font=("Courier", 30, "normal"))
