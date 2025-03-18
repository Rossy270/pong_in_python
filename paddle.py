from turtle import Turtle

PADDLE_SPEED = 10
STRETCH_WIDTH = 4
STRETCH_LEN = 1
PADDLE_OFFSET = [40, 50]

class Paddle(Turtle):
    def __init__(self, pos_origin = (0,0) ,up_key = "Up", down_key = "Down", screen_height = 400):
        super().__init__()

        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid = STRETCH_WIDTH, stretch_len = STRETCH_LEN)
        self.goto(pos_origin)
        self.setheading(90)
        self.tiltangle(-90)
        self.hit_bal = False

        self.up_key = up_key
        self.down_key = down_key
        self.screen_height = screen_height


    def up(self):
        if self.ycor() + PADDLE_OFFSET[0] < self.screen_height:
            self.forward(PADDLE_SPEED)

    def down(self):
        if self.ycor() - PADDLE_OFFSET[1] > - self.screen_height:
            self.backward(PADDLE_SPEED)
