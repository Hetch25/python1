from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('navy')
screen.title("Pong GAME")
screen.tracer(0)


r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))

#lets define what is going to do both paddles
screen.listen()
#player1
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')

#player2
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')

#let's create our scoreboard
scoreboard = Scoreboard()

ball = Ball()   

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()
    
    #detect collision with wall_y
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce_y()

    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30:
        ball.bounce_x()

    

    #detect R_player misses a ball
    if ball.xcor() == 400:
        ball.reset()
        scoreboard.increase_l_score()

    if ball.xcor() == -400:
        ball.reset()
        scoreboard.increase_r_score()




screen.mainloop()