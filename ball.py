import random
from turtle import Turtle
from constants import SCREEN_HEIGHT

X_MOVE_SPEED = 5
Y_MOVE_SPEED = 5
BALL_MARGIN = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.respawn()

    def move(self):
        if self.check_if_bound():
            self.y_speed *= -1

        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto((new_x, new_y))

    def check_if_bound(self):
        y_limit = SCREEN_HEIGHT / 2
        return self.ycor() + BALL_MARGIN > y_limit or self.ycor() - BALL_MARGIN < - y_limit

    def bounce(self):
        self.x_speed *= -1
        if self.x_speed < 8:
            self.x_speed += self.x_speed * 1.2

    def respawn(self):
        self.goto(0,0)
        self.x_speed = random.choice([-X_MOVE_SPEED, X_MOVE_SPEED])
        self.y_speed = random.choice([-Y_MOVE_SPEED, Y_MOVE_SPEED])

