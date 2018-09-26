#-------------------------------------------------------------------------------
# Name:        chpt10./
# Purpose:
#
# Author:      stevb6686
#
# Created:     06/12/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import choice, randrange

# True/False:
# 1. True
# 2. False
# 3. False
# 4. False
# 5. False
# 6. True
# 7. False
# 8. False
# 9. False
# 10. True

# Multiple Choice:
# 1. b
# 2. c
# 3. d
# 4. b
# 5. c
# 6. d
# 7. c
# 8. a
# 9. c
# 10. c

# Programming Exercises:

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w,h = width/2.0, height/2.5
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
    def setColour(self):
        "Sets the colour"

def createWindow():
    win = GraphWin("Encoder/Decoder",400,400)
    win.setCoords(0,0,400,400)
    box = Entry(Point(200,250),40)
    box.draw(win)
    Text(Point(200,285),"Message:").draw(win)
    key = Entry(Point(200,200),5)
    key.draw(win)
    Text(Point(150,200),"Key:").draw(win)
    eButton = Button(win,Point(100,100),75,75,"Encode")
    eButton.activate()
    dButton = Button(win,Point(200,100),75,75,"Decode")
    dButton.activate()
    qButton = Button(win,Point(300,100),75,75,"Quit")
    qButton.activate()
    return win, box, key, eButton, dButton, qButton

def encode(alphabet,key,message,box):
    encode = ""
    for ch in message:
        encode = encode + alphabet[(alphabet.find(ch) + key) % 95]
    box.setText(encode)
    return encode

def decode(alphabet,key,message,box):
    decode = ""
    for ch in message:
        decode = decode + alphabet[(alphabet.find(ch) - key) % 95]
    box.setText(decode)
    return decode

def main2():
    try:
        alphabet = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        win, box, key, eButton, dButton, qButton = createWindow()
        pt = win.getMouse()
        while not qButton.clicked(pt):
            message = box.getText()
            if key.getText() != "":
                newkey = eval(key.getText())
                if eButton.clicked(pt):
                    encode(alphabet,newkey,message,box)
                elif dButton.clicked(pt):
                    decode(alphabet,newkey,message,box)
            pt = win.getMouse()
    except:
        print("Program terminated.")
    win.close()

#-------------------------------------------------------------------------------

def drawWindow():
    win = GraphWin("Three Button Monte",800,600)
    win.setCoords(0,0,800,600)
    door1 = Button(win,Point(200,300),120,240,"Door 1")
    door2 = Button(win,Point(400,300),120,240,"Door 2")
    door3 = Button(win,Point(600,300),120,240,"Door 3")
    door1.activate()
    door2.activate()
    door3.activate()
    qb = Button(win,Point(400,150),80,80,"Quit")
    qb.activate()
    return win, door1, door2, door3, qb

def randomDoor(d1,d2,d3):
    dwin = choice([d1,d2,d3])
    if dwin == d1:
        winner = "1"
    elif dwin == d2:
        winner = "2"
    else:
        winner = "3"
    return dwin, winner

def main4():
    win, door1, door2, door3, qb = drawWindow()
    score = Text(Point(400,500),"")
    score.draw(win)
    correct = Text(Point(400,450),"")
    correct.draw(win)
    wins = 0
    loss = 0
    wincount = Text(Point(200,100),"wins: {}".format(wins))
    losscount = Text(Point(275,100),"losses: {}".format(loss))
    wincount.draw(win)
    losscount.draw(win)
    p = win.getMouse()
    while not qb.clicked(p):
        dwin, winner = randomDoor(door1,door2,door3)
        if door1.clicked(p) or door2.clicked(p) or door3.clicked(p):
            if door1.clicked(p) and door1 == dwin:
                score.setText("You win!")
                wins = wins + 1
            elif door2.clicked(p) and door2 == dwin:
                score.setText("You win!")
                wins = wins + 1
            elif door3.clicked(p) and door3 == dwin:
                score.setText("You win!")
                wins = wins + 1
            else:
                score.setText("You lost!")
                correct.setText("The correct door was door {0}".format(winner))
                loss = loss + 1
        p = win.getMouse()
        score.setText("")
        correct.setText("")
        wincount.setText("wins: {}".format(wins))
        losscount.setText("losses: {}".format(loss))
    win.close()

#-------------------------------------------------------------------------------

def convertToGrade(lgrade):
    lgrade = lgrade.lower()
    d = {"a+":4.3, "a":4.0, "a-":3.7, "b+":3.4, "b":3.1, "b-":2.8, "c+":2.5, "c":2.2, "c-":1.9, "d+":1.6, "d":1.3, "d-":1.0, "f":0.0}
    grade = d[lgrade]
    return grade

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradepoint, credits):
        grade = float(gradepoint)/float(credits)
        return grade

    def __convertToGrade(self, lgrade):
        lgrade = lgrade.lower()
        d = {"a+":4.3, "a":4.0, "a-":3.7, "b+":3.4, "b":3.1, "b-":2.8, "c+":2.5, "c":2.2, "c-":1.9, "d+":1.6, "d":1.3, "d-":1.0, "f":0.0}
        grade = d[lgrade]
        return grade

    def addLetterGrade(self, lgrade, credits):
        gradepoint = self.__convertToGrade(lgrade)
        grade = gradepoint/float(credits)
        return grade

def main6():
    s1 = Student("007",0,0)
    gpoint, credit = (input("Enter the student's gradepoint, and credits (separated by a comma):")).split(",")
    grade = s1.addLetterGrade(gpoint, credit)
    print("The final GPA achieved was {0:0.2f}".format(grade))

#-------------------------------------------------------------------------------

class DieView:

    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):

        """Create a view of a die, e.g.:
        d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""
        # first define some standard values
        self.win = win # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 2.0 # half the size of the die
        offset = 0.6 * hsize # distance from center to outer pips
        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)
        # Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        # Draw an initial value
        self.setValue(1)
        self.value = 1

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.value = 1
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.value = 2
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.value = 3
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.value = 4
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.value = 5
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.value = 6
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

def main8():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
            die1.setColor(color_rgb(randrange(0,257),randrange(0,257),randrange(0,257)))
            die2.setColor(color_rgb(randrange(0,257),randrange(0,257),randrange(0,257)))
        pt = win.getMouse()

    # close up shop
    win.close()

#-------------------------------------------------------------------------------

class Cube:

    def __init__(self, length):
        self.length = eval(length)
        self.surfaceArea = self.length**2 * 6
        self.volume = self.length**3

    def getSurfaceArea(self):
        return self.surfaceArea

    def getVolume(self):
        return self.volume

    def setLength(self, length):
        self.length = eval(length)
        self.surfaceArea = self.length**2 * 6
        self.volume = self.length**3

def main10():
    print("This program calculates the volume and surface area of a cube, given its side length.")
    length = input("Enter the side length:")
    c1 = Cube(length)
    sa = c1.getSurfaceArea()
    v = c1.getVolume()
    print("The surface area is: {}\nThe volume is {}".format(sa,v))

#-------------------------------------------------------------------------------

class Card:

    """A card class that represents a card from the standard poker deck"""

    def __init__(self, rank, suit, center):
        """Creates a card with rank being an int representing Ace - King (1-13)
        and suit being a one letter string representing
        diamonds, clubs, hearts, or spades (d,c,h,s)"""
        self.rank = rank
        self.suit = suit
        self.center = center
        self.x, self.y = self.center.getX(), self.center.getY()
        self.xmin = self.x - 63 # Rounded width/2 of the image
        self.xmax = self.x + 63
        self.ymin = self.y - 91 # Round height/2 of the image
        self.ymax = self.y + 91
        self.p1 = Point(self.xmin,self.ymin)
        self.p2 = Point(self.xmax,self.ymax)
        self.name = self.__str__()
        self.image = "poker_cards\{0}.gif".format(self.name)

    def getRank(self):
        "Returns the rank of a card"
        return self.rank

    def getSuit(self):
        "Returns the suit of a card"
        return self.suit

    def setRank(self, rank):
        "Sets the rank of a card"
        self.rank = rank

    def setSuit(self, suit):
        "Sets the suit of a card"
        self.suit = suit

    def BJValue(self):
        "Returns the Blackjack value of a card"
        if self.rank <= 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        "Returns a string that displays the name of the card"
        drank = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"][self.rank-1]
        dsuit = {"d": "Diamonds", "c": "Clubs", "h": "Hearts", "s": "Spades"}[self.suit.lower()]
        return "{0} of {1}".format(drank,dsuit)

    def draw(self, win):
        "Draws the respective cardface to a graphical window"
        self.cardface = Image(self.center,self.image)
        self.cardface.draw(win)

    def move(self, dx, dy):
        "Moves the card object in a graphical window"
        self.cardface.move(dx,dy)
        self.center = Point(self.x + dx, self.y + dy)
        self.x, self.y = self.center.getX(), self.center.getY()
        self.xmin = self.x - 63 # Rounded width/2 of the image
        self.xmax = self.x + 63
        self.ymin = self.y - 91 # Round height/2 of the image
        self.ymax = self.y + 91
        self.p1 = Point(self.xmin,self.ymin)
        self.p2 = Point(self.xmax,self.ymax)

    def faceup(self, win):
        "Sets the card to face up"
        if not hasattr(self, "draw"):
            self.cardface.undraw()
        self.cardface = Image(self.center, self.image)
        self.cardface.draw(win)

    def facedown(self, win):
        "Sets the card to face down"
        if not hasattr(self, "draw"):
            self.cardface.undraw()
        self.cardface = Image(self.center, "poker_cards\\Card Back.gif")
        self.cardface.draw(win)

    def animate(self, point, t, win):
        "Animates the card moving to the point in the specified time"
        dx = point.getX() - self.center.getX()
        dy = point.getY() - self.center.getY()
        vx = dx/t
        vy = dy/t
        movx = vx * 0.016
        movy = vy * 0.016

        # Test if the current card position has moved past the intended distance
        while (((dx >= 0 and point.getX() - self.center.getX() >= 0) or (dx <= 0 and point.getX() - self.center.getX() <= 0))
        and ((dy >= 0 and point.getY() - self.center.getY() >= 0) or (dy <= 0 and point.getY() - self.center.getY() >= 0))):
            self.move(movx, movy)
            time.sleep(0.016)

        # Snap to finish point
        dx = point.getX() - self.center.getX()
        dy = point.getY() - self.center.getY()
        self.move(dx, dy)



def main11():
    print("This program pulls randomly generated poker cards and prints their Blackjack value.")
    n = eval(input("Enter the number of cards to randomly generate:"))
    for i in range(n):
        card = Card(randrange(1,14),choice(["d","c","h","s"]))
        print("{0}. Blackjack value = {1}".format(card, card.BJValue()))

#-------------------------------------------------------------------------------

def makeWindow():
    win = GraphWin("Poker Cards",800,600)
    win.setCoords(0,0,800,600)
    return win


def main12():
    win = makeWindow()
    x = 100
    y = 260
    for i in range(5):
        c = Card(randrange(1,14),choice(["d","c","h","s"]),Point(x,y))
        c.draw(win)
        for i in range(20):
            c.move(5,2)
            time.sleep(0.001)
        x = x + 100
    c.facedown(win)
    c.animate(Point(400,300),1,win)
    win.getMouse()
    win.close()

#-------------------------------------------------------------------------------