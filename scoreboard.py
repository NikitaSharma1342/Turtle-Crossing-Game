from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        with open ('data.txt', 'r') as data:
            self.highest_level = int(data.read())
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(-280, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.level > self.highest_level:
            self.highest_level = self.level
            with open('data.txt','w') as data:
                data.write(f"{self.highest_level}")
        self.clear()
        self.write(f"Level: {self.level}    Highest Level: {self.highest_level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
