from turtle import Turtle
from constants import SCREEN_HEIGHT

SCORE_FONT = ("Arial", 32, "bold")
SCORE_ALIGN = "center"
WIDTH_GAPPING = 50
HEIGHT_GAPPING = 60

class ScoreBoard:
    def __init__(self):
        super().__init__()
        self.line_turtle = None
        self.r_text = None
        self.l_text = None
        self.r_score = 0
        self.l_score = 0
        self.draw_middle_line()
        self.initial_score_text()

    def draw_middle_line(self):
        self.line_turtle = Turtle()
        self.line_turtle.color("white")
        self.line_turtle.pensize(10)
        self.line_turtle.right(90)
        self.line_turtle.penup()
        self.line_turtle.goto(0, SCREEN_HEIGHT / 2)
        self.line_turtle.pendown()
        for i in range(20):
            self.line_turtle.forward(10)
            self.line_turtle.penup()
            self.line_turtle.forward(20)
            self.line_turtle.pendown()

    def initial_score_text(self):
        score_y_pos = (SCREEN_HEIGHT / 2) - HEIGHT_GAPPING
        self.r_text = Turtle()
        self.r_text.hideturtle()
        self.r_text.color("white")
        self.r_text.penup()
        self.r_text.goto(WIDTH_GAPPING, score_y_pos)
        self.r_text.write(f"{self.r_score}", font = SCORE_FONT, align = SCORE_ALIGN)

        self.l_text = Turtle()
        self.l_text.hideturtle()
        self.l_text.color("white")
        self.l_text.penup()
        self.l_text.goto(-WIDTH_GAPPING, score_y_pos)
        self.l_text.write(f"{self.l_score}", font=SCORE_FONT, align=SCORE_ALIGN)

    def update_score(self, r_paddle_score = False, l_paddle_score = False):
        if r_paddle_score:
            self.r_score += 1
            self.r_text.clear()
            self.r_text.write(f"{self.r_score}", font=SCORE_FONT, align=SCORE_ALIGN)
        if l_paddle_score:
            self.l_score += 1
            self.l_text.clear()
            self.l_text.write(f"{self.l_score}", font=SCORE_FONT, align=SCORE_ALIGN)

    def game_end(self, r_win: False):
        who_win = "Player 1" if r_win else "Player 2"
        self.line_turtle.clear()
        self.line_turtle.goto(0,0)
        self.line_turtle.write(f"Parabens ao jogador {who_win}\n" + " " * 11 +"Você ganhou!!!", font = ("Arial", 18, "bold"), align = SCORE_ALIGN)
