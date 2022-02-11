from turtle import *

timmy = Turtle()
screen = Screen()

for _ in range(11):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()