from turtle import Turtle
MOVE_DISTANCE = 20



class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)
        self.color("white")

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

