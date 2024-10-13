from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

#animating(moving) the snake
game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend_body()
                score.increment_score()


        #detect collision with wall
        if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
                score.reset_scoreboard()
                snake.reset_snake()


        #detect collision with tail
        for segment in snake.segments[1:]:                
                if snake.head.distance(segment) < 10:
                        score.reset_scoreboard()
                        snake.reset_snake()

screen.exitonclick()
