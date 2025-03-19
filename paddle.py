from turtle import Turtle
from constants import SCREEN_HEIGHT

MOVE_SPEED = 20
PADDLE_OFFSET = [40, 70]

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.hit_paddle = False
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() + PADDLE_OFFSET[0] < SCREEN_HEIGHT / 2:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)


    def down(self):
        if self.ycor() - PADDLE_OFFSET[1] > - SCREEN_HEIGHT / 2:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
