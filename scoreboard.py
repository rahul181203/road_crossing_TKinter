import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()        
    
    def update_score(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"level: {self.level}",align="left",font=FONT)
        self.goto(0,250)
        self.write(f"score: {self.score}",align="center",font=FONT)
    
    def score_plus(self):
        self.score += 1
        self.level += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)