from turtle import Turtle

filename = "../100 days of python code/Day20(snake game)/snakedata.txt"
with open(filename) as f:
    score = int(f.read())
    print(score)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = score
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(arg=f'SCORE: {self.score}', align='center', font=('Arial', 18, 'bold'))
        self.hideturtle()
        self.update_score()
        

    def update_score(self):      
        self.clear()
        with open(filename, "w") as f:
            f.write(f"{self.highscore}") 
        self.write(arg=f'SCORE : {self.score} -- High Score : {self.highscore}', align='center', font=('Arial', 18, 'bold'))


    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write(arg=f'Game over', align='center', font=('Arial', 18, 'bold'))

    def increment_score(self):
        self.score += 1
        self.update_score()
        
        


     

