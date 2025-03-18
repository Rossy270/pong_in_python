from turtle import Turtle

WIDTH_PADDING = 50
HEIGHT_PADDING = 60

SCORE_FONT = ("Arial", 32, "bold")
ALIGN_FONT = "center"

WIN_FONT = ("Robot", 36, "bold")

class UI:
    def __init__(self, screen_size):
        self.height = screen_size[1] / 2
        self.draw_middle_line()
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_text_score = Turtle()
        self.player_2_text_score = Turtle()
        self.initial_score()

    def initial_score(self):
        #criando a score do player 1
        self.player_1_text_score.clear()
        self.player_1_text_score.color("white")
        self.player_1_text_score.penup()
        self.player_1_text_score.hideturtle()
        self.player_1_text_score.goto((-WIDTH_PADDING, self.height - HEIGHT_PADDING))
        self.player_1_text_score.write(f"{self.player_1_score}",font=SCORE_FONT, align=ALIGN_FONT)

        #Criando o score do player 2
        self.player_2_text_score.clear()
        self.player_2_text_score.color("white")
        self.player_2_text_score.penup()
        self.player_2_text_score.hideturtle()
        self.player_2_text_score.goto((WIDTH_PADDING, self.height - HEIGHT_PADDING))
        self.player_2_text_score.write(f"{self.player_2_score}", font=SCORE_FONT, align=ALIGN_FONT)

    def draw_middle_line(self):
        self.middle_line = Turtle()
        self.middle_line.color("white")
        self.middle_line.pensize(10)
        self.middle_line.penup()
        self.middle_line.right(90)
        self.middle_line.goto((0, self.height - 10))
        self.middle_line.pendown()
        for i in range(10):
            self.middle_line.forward(20)
            self.middle_line.penup()
            self.middle_line.forward(20)
            self.middle_line.pendown()

    def update_score(self, who_score):
        match who_score:
            case "player_1":
                self.player_1_score += 1
            case "player_2":
                self.player_2_score += 1

        self.player_1_text_score.clear()
        self.player_1_text_score.write(f"{self.player_1_score}",font=("Arial", 32, "bold"), align="center")

        self.player_2_text_score.clear()
        self.player_2_text_score.write(f"{self.player_2_score}",font=("Arial", 32, "bold"), align="center")

    def show_winner(self, who_win):
        match who_win:
            case "player_1":
                self.clear_line()
                self.middle_line.write("Player 1 Win!!!!", font=WIN_FONT, align="center")
            case "player_2":
                self.clear_line()
                self.middle_line.write("Player 2 Win!!!!", font=WIN_FONT, align="center")


    def clear_line(self):
        self.middle_line.clear()
        self.middle_line.goto((0,0))







        