from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player1_paddle = Paddle(x_cor=-350, y_cor=0)
player2_paddle = Paddle(x_cor=350, y_cor=0)

screen.listen()
screen.onkey(player1_paddle.move_w, "w")
screen.onkey(player1_paddle.move_s, "s")
screen.onkey(player2_paddle.move_up, "Up")
screen.onkey(player2_paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
