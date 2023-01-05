import turtle

# window creation
wn = turtle.Screen()
wn.setup(1000, 1000)
wn.title("CHECKERS")
wn.bgcolor("lightgreen")
wn.tracer(0)

# list for all board classes
board = []

# pen used for drawing on screen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# global variables
class Global:
    firstSelection = True
    # if userTurn = False then it is greens turn
    # if userTurn = True then it is blues turn
    userTurn = True

globalVar = Global()

class Board:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.positionalX = (self.x * 80) - 320
        self.positionalY = (self.y * 80) - 320
        self.selectedFirst = False
        self.selectedSecond = False
        self.highlight = False
        self.containsBlue = False
        self.containsGreen = False
        self.defaultColor = color
        self.color = self.defaultColor


    def drawBoard(self):
        if self.selectedFirst:
            self.color = 'yellow'

        if self.highlight:
            self.color = 'lightblue'

        pen.goto(self.positionalX, self.positionalY)
        pen.shape("square")
        pen.color(self.color)
        pen.shapesize(4)
        pen.stamp()

        if self.containsBlue:
            pen.goto(self.positionalX, self.positionalY)
            pen.shape("circle")
            pen.color("blue")
            pen.shapesize(3)
            pen.stamp()

        if self.containsGreen:
            pen.goto(self.positionalX, self.positionalY)
            pen.shape("circle")
            pen.color("green")
            pen.shapesize(3)
            pen.stamp()


# click functions
def highlightClick(x, y):
    # first we have to find out whose click it was
    if globalVar.userTurn:
        # This means that the click was on blues side
        # now we have to see if it is the users first click
        if globalVar.firstSelection:
            # this means that blue is clicking to select
            # we must check if the click was in a square that contains blue
            for square in board:
                if square.x == x and square.y == y:
                    if square.containsBlue:
                        print("this is a possible square to primary select")
                        globalVar.firstSelection = False
                        break
                    else:
                        globalVar.firstSelection = True
                else:
                    globalVar.firstSelection = True
        elif not globalVar.firstSelection:
            # this means that blue has clicked for a second time
            for square in board:
                if square.x == x and square.y == y:
                    print("this is a possible square to secondary select")

            globalVar.firstSelection = True

def findClickLocation(x, y):
    gridX = round((x + 320) / 80)
    gridY = round((y + 320) / 80)
    print(gridX + 1, gridY + 1)

    highlightClick(gridX, gridY)

# board generation
for i in range(8):
    for j in range(8):
        if (i + j) % 2 != 0:
            color = "red"
        else:
            color = "black"


        square = Board(i, j, color)
        if j == 0 and i % 2 == 0:
            square.containsBlue = True
        if j == 1 and i % 2 != 0:
            square.containsBlue = True
        if j == 2 and i % 2 == 0:
            square.containsBlue = True

        if j == 5 and i % 2 != 0:
            square.containsGreen = True
        if j == 6 and i % 2 == 0:
            square.containsGreen = True
        if j == 7 and i % 2 != 0:
            square.containsGreen = True

        board.append(square)

# draw board
for square in board:
    square.drawBoard()

# on screen click event
wn.onscreenclick(findClickLocation, 1)

# main loop function
wn.mainloop()