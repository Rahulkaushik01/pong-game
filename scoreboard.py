from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('courier', 80, 'normal'))

    def score1(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def score2(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

