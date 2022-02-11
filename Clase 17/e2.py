from turtle import *
import random

line = Turtle()
screen = Screen()

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
 
    return (r,g,b)

#first way
line.pensize(width=15)
line.speed('fastest')
def draw1():
    angle = random.randint(0,3) * 90
    line.forward(30)
    line.setheading(angle)
    line.color(random_color())

'''for _ in range(10000):
    draw1()'''

#second way
directions = [0,90,180,270]
def draw2():
    line.forward(30)
    line.setheading(random.choice(directions))
    line.color(random_color())

for _ in range(10000):
    draw2()

