from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.up()
        self.goto(x=0,y=260)
        # self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal")) will lead to overlap
        # self.color("white") # if we write here still its in black
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore: {self.highscore}", align=ALIGN, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear() # to avoid overlapping of scores
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over!!", align=ALIGN, font=FONT)




