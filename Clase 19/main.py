from turtle import Turtle, Screen, width
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)


#Create a snake
snake= Snake()
food= Food()
scoreboard = Scoreboard()

#lets code the methods to be able to move our snake
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect when happen a collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #detect when happen a collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.GameOver()
        game_is_on = False

    #detect when snake hit itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 4:
            scoreboard.GameOver()
            game_is_on = False



screen.mainloop()