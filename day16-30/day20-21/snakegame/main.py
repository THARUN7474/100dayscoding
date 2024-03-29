from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        is_on=False
        score.game_over()

    for seg in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[seg]) < 10:
            is_on = False
            score.game_over()


screen.exitonclick()