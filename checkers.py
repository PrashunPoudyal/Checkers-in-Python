# imports turtle function
# turtle functions has all graphics information
import turtle

# window creation
wn = turtle.Screen()
# window name is wn
# window will be 1000 px by 1000px
wn.setup(1000, 1000)
# window title will be CHECKERS
wn.title("CHECKERS")
# window background colour will be lightgreen
wn.bgcolor("lightgreen")
# the window tracer tells the turtle graphics how screen updates will occur. putting tracer as 0 will make it so that the
# programming determines when to update the screen
wn.tracer(0)

# pen used for drawing on screen
# the way the pen will work is everytime it needs to draw something, the class instance will call on the pen to its
# location and the pen will change its shape and colour to match the class instance, and then stamp that design onto the screen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# textWriter is the part of the screen that will include all the text information
textWriter = turtle.Turtle()
textWriter.penup()
textWriter.hideturtle()

# global variables
# Although this isnt the best way to do global variables, we put all global variables into a class called Global
class Global:
    # this boolean variable determines if the click is the first click or the second click
    firstSelection = True
    # this are the grid coordinates of the first selected grid and will change constantly
    # when the grid has -1, -1, that means that no grid has been selected
    selectedGrid = (-1, -1)
    # if userTurn = False then it is greens turn
    # if userTurn = True then it is blues turn
    userTurn = True
    # this is where all the class instances are stored
    board = []

    remainingBluePieces = 12
    remainingGreenPieces = 12

# creation of Global class instance
globalVar = Global()


class BackgroundUI:
    def __init__(self):
        self.color = 'grey'
        self.shape = 'square'
        self.x = 0
        self.y = 400

    def drawUI(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color('black', self.color)
        pen.shapesize(10, 55)
        pen.stamp()


class TurnUI:
    def __init__(self):
        self.color = 'grey'
        self.shape = 'square'
        self.x = 275
        self.y = 435

    def drawUI(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color('black', self.color)
        pen.shapesize(5, 20)
        pen.stamp()


class GreenDeathCounter:
    def __init__(self):
        self.color = 'grey'
        self.shape = 'square'
        self.x = -270
        self.y = 450

    def drawUI(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color('black', self.color)
        pen.shapesize(3, 20)
        pen.stamp()


class BlueDeathCounter:
    def __init__(self):
        self.color = 'grey'
        self.shape = 'square'
        self.x = -270
        self.y = 350

    def drawUI(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color('black', self.color)
        pen.shapesize(3, 20)
        pen.stamp()


class BlueCircles:
    def __init__(self, number):
        self.number = number

    def drawCircle(self, pen):
        pen.goto(-450+(self.number * 30) - 20, 450)
        pen.shape("circle")
        pen.shapesize(1)
        pen.color("black", "#a86c4a")
        pen.stamp()


class GreenCircles:
    def __init__(self, number):
        self.number = number

    def drawCircle(self, pen):
        pen.goto(-450+(self.number * 30) - 20, 350)
        pen.shape("circle")
        pen.shapesize(1)
        pen.color("black", "#f0e3a9")
        pen.stamp()

# this is the board class

'''
originally we had the idea to make a class for the board and make a class for the checker pieces.

after trying it out, we realized it would be a lot easier if we just made one class which is the board, and the board
has different states which are:
    1. empty
    2. containsBlue
    3. containsGreen

this is a lot more optimized and easier to program with
'''
class Board:
    def __init__(self, x, y, color):
        '''
        :param x: x coordinate
        :param y: y coordinate
        :param color: red or black checkerboard pattern

        the variables listed below are used for the following things

        x is the x coordinate of the grid in relation to other squares. This means that the max x is 7 because it starts
        at 0, resulting in 8 different x squares.

        y is the y coordinate of the grid in relation to other squares. This means that the max y is 7 beecause it starts
        at 0, resulting in 8 different y squares.

        combined with the x and y this means there are 64 squares on the map at any given time

        positionalX and positionalY are where the squares are truly in relation to the screen

        this means the proper x and y coordinates of the boxes.

        selectedFirst determines if the square in question has been selected and whether or not it was the first
        selection or the second

        selectedSecond determines if the square in question has been selected and whether or not it was the first
        selection or the second

        highlight determines whether or not the square in question should be highlighted

        containsBlue is one of the three states of the square
        containsGreen is one of the three states of the square

        defaultColor is either red or black. it is there because in the event that a square gets highlighted, it will have
        to revert back to its default colour, and so it stores that information so that it doesnt get forgotten

        color is the current colour, which could be the highlighted colour, or the proper colour.
        '''
        self.x = x
        self.y = y
        self.positionalX = (self.x * 80) - 320
        self.positionalY = (self.y * 80) - 320
        self.selectedFirst = False
        self.selectedSecond = False
        self.highlight = False
        self.containsBlue = False
        self.containsGreen = False
        self.isKing = False
        self.defaultColor = color
        self.color = self.defaultColor


    def drawBoard(self):
        '''
        this function draws the board onto the screen.

        it does so by calling the pen instance and assigns the pen all the attributes that the square in question has

        once it does this the pen will stamp that appearance onto the screen
        '''
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
            pen.color("black", "#a86c4a")
            pen.shapesize(3)
            pen.stamp()

        if self.containsGreen:
            pen.goto(self.positionalX, self.positionalY)
            pen.shape("circle")
            pen.color("black", "#f0e3a9")
            pen.shapesize(3)
            pen.stamp()


def updateDeathCounter():
    deadGreenPieces = (globalVar.remainingGreenPieces - 12) * -1
    deadBluePieces = (globalVar.remainingBluePieces - 12) * -1

    if deadBluePieces:
        circle = BlueCircles(deadBluePieces)
        circle.drawCircle(pen)
        print("circle created")

    if deadGreenPieces:
        circle = GreenCircles(deadGreenPieces)
        circle.drawCircle(pen)
        print("circle created")


def showWhoseTurn():
    textWriter.clear()
    textWriter.goto(95, 395)
    if not globalVar.userTurn:
        textWriter.write("WHITE TURN", font=("Courier", 45, 'bold'))
    else:
        textWriter.write("BLACK TURN", font=("Courier", 45, 'bold'))

# all functions that relate to legality


def spaceLimiter(firstSquare, secondSquare, killException):

    if firstSquare.containsGreen:
        if not killException:

            firstSquareGrid = (firstSquare.x, firstSquare.y)
            secondSquareGrid = (secondSquare.x, secondSquare.y)

            if not (secondSquareGrid[1] - firstSquareGrid[1]) == 1:
                # this means that the second square is not one rank away (positively)

                if not ((secondSquareGrid[0] - firstSquareGrid[0]) == 1 or (secondSquareGrid[0] - firstSquareGrid[0]) == -1):
                    # this means that the second square is not one file away (positively or negatively)
                    return False

        if killException:

            firstSquareGrid = (firstSquare.x, firstSquare.y)
            secondSquareGrid = (secondSquare.x, secondSquare.y)

            xDifference = secondSquareGrid[0] - firstSquareGrid[0]

            if not (secondSquareGrid[1] - firstSquareGrid[1]) == 2:
                # this means that the second square is not two ranks away (positively)
                if not ((secondSquareGrid[0] - firstSquareGrid[0]) == 2 or (secondSquareGrid[0] - firstSquareGrid[0]) == -2):
                    # this means that the second square is not two files away (positively or negatively)
                    return False

            for square in globalVar.board:
                if square.y == firstSquareGrid[1] - 1:
                    if xDifference > 0:
                        if square.x == firstSquareGrid[0] + 1:
                            square.containsBlue = False
                            globalVar.remainingBluePieces -= 1
                            square.drawBoard()

                    if xDifference < 0:
                        if square.x == firstSquareGrid[0] - 1:
                            square.containsBlue = False
                            globalVar.remainingBluePieces -= 1
                            square.drawBoard()

    if firstSquare.containsBlue:
        if not killException:

            firstSquareGrid = (firstSquare.x, firstSquare.y)
            secondSquareGrid = (secondSquare.x, secondSquare.y)

            if not (secondSquareGrid[1] - firstSquareGrid[1]) == -1:
                # this means that the second square is not one rank away (positively)
                if not ((secondSquareGrid[0] - firstSquareGrid[0]) == 1 or (secondSquareGrid[0] - firstSquareGrid[0]) == -1):
                    # this means that the second square is not one file away (positively or negatively)
                    return False

        if killException:

            firstSquareGrid = (firstSquare.x, firstSquare.y)
            secondSquareGrid = (secondSquare.x, secondSquare.y)

            xDifference = secondSquareGrid[0] - firstSquareGrid[0]

            if not (secondSquareGrid[1] - firstSquareGrid[1]) == -2:
                # this means that the second square is not two ranks away (positively)
                if not ((secondSquareGrid[0] - firstSquareGrid[0]) == 2 or (secondSquareGrid[0] - firstSquareGrid[0]) == -2):
                    # this means that the second square is not two files away (positively or negatively)
                    return False

            for square in globalVar.board:
                if square.y == firstSquareGrid[1] + 1:
                    if xDifference > 0:
                        if square.x == firstSquareGrid[0] + 1:
                            square.containsGreen = False
                            globalVar.remainingGreenPieces -= 1
                            square.drawBoard()

                    if xDifference < 0:
                        if square.x == firstSquareGrid[0] - 1:
                            square.containsGreen = False
                            globalVar.remainingGreenPieces -= 1
                            square.drawBoard()

    return True


def findKillException(firstSquare, secondSquare):
    # before we begin killException process we have to determine if it is blue piece or green piece
    if firstSquare.containsGreen:
        # first we need to find the x difference between firstSquare and secondSquare should be + 2 or - 2
        xDifference = secondSquare.x - firstSquare.x

        # because it is a green square the y must have a difference of -2
        # that means we have to check if there is an opposing colour square within -1 y of the primary move
        for square in globalVar.board:
            if square.containsBlue:
                if square.y == firstSquare.y - 1:
                    # then we have to check if there is a square to the same diagonal as the secondSquare
                    if xDifference > 0: # positive integer
                        if square.x == firstSquare.x + 1:
                            return True

                    if xDifference < 0:
                        if square.x == firstSquare.x - 1:
                            return True

    if firstSquare.containsBlue:
        xDifference = secondSquare.x - firstSquare.x

        for square in globalVar.board:
            if square.containsGreen:
                if square.y == firstSquare.y + 1:

                    if xDifference > 0:
                        if square.x == firstSquare.x + 1:
                            return True

                    if xDifference < 0:
                        if square.x == firstSquare.x - 1:
                            return True

    return False



    # now we have to find out if there is a piece in between these two pieces


def checkIfLegal(firstSquare, secondSquare):
    # makes sure that the only legal move is in a black square
    if (secondSquare.x + secondSquare.y) % 2 != 0:
        return False
    else:
        pass

    # make sure that the player is not moving in a location with an already existing square
    for square in globalVar.board:
        if square.x == secondSquare.x and square.y == secondSquare.y:
            if square.containsBlue == True or square.containsGreen == True:
                return False
            else:
                continue

    # check if killException flag is necessary

    killException = findKillException(firstSquare, secondSquare)

    print("kill exception: " + str(killException))

    # only allow moves that are one space away unless there are exceptions
    spaceLimitFlag = spaceLimiter(firstSquare, secondSquare, killException)

    print(firstSquare.x, firstSquare.y)
    print(secondSquare.x, secondSquare.y)


    if not spaceLimitFlag:
        return False

    print(globalVar.remainingGreenPieces)
    print(globalVar.remainingBluePieces)

    updateDeathCounter()

    return True

# click functions
def highlightClick(x, y):
    # first we have to find out whose click it was
    if globalVar.userTurn:
        # This means that the click was on blues side
        # now we have to see if it is the users first click
        if globalVar.firstSelection:
            # this means that blue is clicking to select
            # we must check if the click was in a square that contains blue
            for square in globalVar.board:
                if square.x == x and square.y == y:
                    if square.containsBlue:
                        print("this is a possible square to primary select")
                        globalVar.selectedGrid = (x, y)
                        globalVar.firstSelection = False
                        break
                    else:
                        globalVar.firstSelection = True
                else:
                    globalVar.firstSelection = True
        elif not globalVar.firstSelection:
            # this means that blue has clicked for a second time
            for square in globalVar.board:
                if square.x == x and square.y == y:
                    primarySquare = None

                    for firstSquare in globalVar.board:
                        if firstSquare.x == globalVar.selectedGrid[0] and firstSquare.y == globalVar.selectedGrid[1]:
                            primarySquare = firstSquare

                    legal = checkIfLegal(primarySquare, square)
                    if legal:
                        print("this is a possible square to secondary select")
                        # updates second square to have a blue checker
                        square.containsBlue = True
                        square.drawBoard()
                        # updates first square to remove blue checker
                        for firstSquare in globalVar.board:
                            if firstSquare.x == globalVar.selectedGrid[0] and firstSquare.y == globalVar.selectedGrid[1]:
                                firstSquare.containsBlue = False
                                firstSquare.drawBoard()
                                globalVar.userTurn = False
                                showWhoseTurn()
                                break

                    break

            globalVar.firstSelection = True

    if not globalVar.userTurn:
        # This means that the click was on green side
        # now we have to see if it is the users first click
        if globalVar.firstSelection:
            # this means that green is clicking to select
            # we must check if the click was in a square that contains blue
            for square in globalVar.board:
                if square.x == x and square.y == y:
                    if square.containsGreen:
                        print("this is a possible square to primary select")
                        globalVar.selectedGrid = (x, y)
                        globalVar.firstSelection = False
                        break
                    else:
                        globalVar.firstSelection = True
                else:
                    globalVar.firstSelection = True
        elif not globalVar.firstSelection:
            # this means that green has clicked for a second time
            for square in globalVar.board:
                if square.x == x and square.y == y:
                    primarySquare = None

                    for firstSquare in globalVar.board:
                        if firstSquare.x == globalVar.selectedGrid[0] and firstSquare.y == globalVar.selectedGrid[1]:
                            primarySquare = firstSquare

                    legal = checkIfLegal(primarySquare, square)
                    if legal:
                        print("this is a possible square to secondary select")
                        # updates second square to have a green checker
                        square.containsGreen = True
                        square.drawBoard()
                        # updates first square to remove blue checker
                        for firstSquare in globalVar.board:
                            if firstSquare.x == globalVar.selectedGrid[0] and firstSquare.y == globalVar.selectedGrid[1]:
                                firstSquare.containsGreen = False
                                firstSquare.drawBoard()
                                globalVar.userTurn = True
                                showWhoseTurn()
                                break

                    break

            globalVar.firstSelection = True


def findClickLocation(x, y):
    '''
    :param x: the x coordinate of the click
    :param y: the y coordinate of the click

    after finding the x and y coordinate of the click, it will convert it into the grid coordinates, then call
    the highlightClick(x, y) function, which will register and compute the click
    '''
    gridX = round((x + 320) / 80)
    gridY = round((y + 320) / 80)
    print(gridX + 1, gridY + 1)

    highlightClick(gridX, gridY)

# board generation
for i in range(8):
    for j in range(8):
        '''
        this is really simple board generation.
        
        it creates an 8 x 8 grid and assigns the proper colour, then creates a class instance with this information
        which will then get stored into globalVar.board list.
        '''
        if (i + j) % 2 != 0:
            color = "#84543c"
        else:
            color = "#d4cc94"


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

        globalVar.board.append(square)

# draw board
for square in globalVar.board:
    square.drawBoard()

background = BackgroundUI()
background.drawUI(pen)

turn = TurnUI()
turn.drawUI(pen)

blueCounter = GreenDeathCounter()
blueCounter.drawUI(pen)

blueCounter = BlueDeathCounter()
blueCounter.drawUI(pen)

# draw information
showWhoseTurn()

# on screen click event
wn.onscreenclick(findClickLocation, 1)

# main loop function
wn.mainloop()
