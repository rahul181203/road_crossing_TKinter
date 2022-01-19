import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)
    
    def restart(self):
        self.goto(STARTING_POSITION)
    
    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False