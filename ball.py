from turtle import Turtle

BALL_Y_OFFSET = 10

class Ball(Turtle):
    def __init__(self, horizontal_speed = -8, vertical_speed = -8, screen_size = (0,0)):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = vertical_speed
        self.dy = horizontal_speed
        self.screen_height = screen_size[1] / 2
        self.screen_width = screen_size[0] / 2
        self.respawn()

    def respawn(self):
        self.goto(0,0)

    def move(self):
        #Checo se a bola acerta o teto ou o chão da quadra
        if self.check_if_hit_floor() or self.check_if_hit_roof():
            self.dy *= -1

        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def collider(self):
        self.dx *= -1

    def check_if_hit_roof(self):
        return self.ycor() + BALL_Y_OFFSET > self.screen_height

    def check_if_hit_floor(self):
        return self.ycor() - BALL_Y_OFFSET < -self.screen_height

    def check_if_someone_scored(self):
        if self.xcor() > self.screen_width:
            return "player_1"
        elif self.xcor() <  - self.screen_width:
            return "player_2"
        else:
            return ""