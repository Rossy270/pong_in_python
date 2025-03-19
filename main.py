from turtle import Screen, textinput
from paddle import Paddle
from ball import Ball
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from scoreboard import ScoreBoard
import time

points_goal = int(textinput(title = "Pong prompt", prompt="until when?: "))

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.up, key="Up")
screen.onkeypress(r_paddle.down, key="Down")
screen.onkeypress(l_paddle.up, key="w")
screen.onkeypress(l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()


    if ball.xcor() > 0 and r_paddle.distance(ball) < 30 and not r_paddle.hit_paddle:
        r_paddle.hit_paddle = True
        ball.bounce()

        if l_paddle.hit_paddle:
            l_paddle.hit_paddle = False

    # noinspection PyTypeChecker
    if ball.xcor() < 0 and l_paddle.distance(ball) < 30 and l_paddle.hit_paddle == False:
        l_paddle.hit_paddle = True
        ball.bounce()

        if r_paddle.hit_paddle:
            r_paddle.hit_paddle = False

    if ball.xcor() < -SCREEN_WIDTH / 2:
        scoreboard.update_score(r_paddle_score = True)
        ball.respawn()
        l_paddle.hit_paddle = False
        r_paddle.hit_paddle = False
    elif ball.xcor() > SCREEN_WIDTH / 2:
        scoreboard.update_score(l_paddle_score = True)
        ball.respawn()
        l_paddle.hit_paddle = False
        r_paddle.hit_paddle = False

    #Checando se alguem ganhou
    if scoreboard.r_score >= points_goal:
        game_is_on = False
        scoreboard.game_end(r_win = True)
    elif scoreboard.l_score >= points_goal:
        game_is_on = False
        scoreboard.game_end(r_win = False)



screen.exitonclick()