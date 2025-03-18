from turtle import Screen
from paddle import Paddle
from ui import UI
from ball import Ball
import time


game_is_on = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def create_screen():
    new_screen = Screen()
    new_screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    new_screen.listen()
    new_screen.title("Pong in Python")
    new_screen.bgcolor("black")
    new_screen.tracer(0)

    return new_screen

#Criando Screen
screen = create_screen()


#Criando os paddle
paddle_p2 = Paddle(pos_origin= (260, 0), screen_height= SCREEN_HEIGHT / 2)
paddle_p1 =  Paddle(pos_origin=(-260,0), up_key="w", down_key="s", screen_height = SCREEN_HEIGHT /2)

#Habilidando input
screen.listen()

screen.onkeypress(fun=paddle_p1.up, key=paddle_p1.up_key)
screen.onkeypress(fun=paddle_p1.down, key=paddle_p1.down_key)
screen.onkeypress(fun=paddle_p2.up, key=paddle_p2.up_key)
screen.onkeypress(fun=paddle_p2.down, key=paddle_p2.down_key)

#criando o HUD (tudo na classe ScoreBoad)
ui = UI((SCREEN_WIDTH, SCREEN_HEIGHT))

#criando a bola
ball = Ball(screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT))

while game_is_on:
    screen.update()
    time.sleep(0.1)

    #Checa se ocorre um ponto
    who_score = ball.check_if_someone_scored()

    if who_score != "":
        ui.update_score(who_score)
        ball.respawn()

    #check se algum paddle enconsta na pola
    if ball.xcor() < 0:
        if paddle_p2.hit_bal:
            paddle_p2.hit_bal = False

        if paddle_p1.distance(ball) < 30 and not paddle_p1.hit_bal:
            ball.collider()
            paddle_p1.hit_bal = True
    elif ball.xcor() > 0:
        if paddle_p1.hit_bal:
            paddle_p1.hit_bal = False

        if paddle_p2.distance(ball) < 30 and not paddle_p2.hit_bal:
            ball.collider()
            paddle_p2.hit_bal = True

    if ui.player_1_score >= 3:
        game_is_on = False
        ui.show_winner(who_score)
    elif ui.player_2_score >= 3:
        game_is_on = False
        ui.show_winner(who_score)


    ball.move()



screen.exitonclick()