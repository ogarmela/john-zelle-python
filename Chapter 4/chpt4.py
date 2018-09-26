#-------------------------------------------------------------------------------
# Name:        Chapter 4
# Purpose:
#
# Author:      stevb6686
#
# Created:     04/10/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import random
import math

# True/False

# 1. False
# 2. True
# 3. True
# 4. False
# 5. True
# 6. False
# 7. True
# 8. False
# 9. False
# 10. False

# Multiple_Choice

# 1. d
# 2. b
# 3. d
# 4. c
# 5. d
# 6. d
# 7. d
# 8. b
# 9. a
# 10.b


# Discussion questions

# 1.
# Object: Convection oven
# attributes:
# Metal
# Rectangular
# Front Window
# Fans
# Handle
# Buttons
# Timer
# Beeper
# methods:
# set temperature of oven
# start beeper at time == 0
# turn on convection current

# 2. (based on default setCoords)
# a) creates a single black pixel (point) at (130,130).
# b) creates a circle at centre point (30,40) with a radius of 25.
# The circle colour is blue, the outline of the circle is red.
# c) creates a bright green square with a large black outline in the top left
# d) creates a 1px width dark red arrow from the bottom middle of the screen to the exact middle with a arrow on the end
# e) creates a vertically skinny hollow oval with a black outline in the top left
# f) creates a tiny hourglass in the top left with an orange fill
# g) shows "Hello world!" in the middle of the window in size 16 courier font in italics.

# 3.
# Creates a red circle in the top left of the window. Then, 10 times over, it waits for a mouse click.
# Once clicked, it moves the red circle to the cursor position by taking the difference between the
# Object's position attribute and the mouse click position. After 10 clicks, the window is closed.

# Programming excercises

def main2():
    win = GraphWin("Archery Target",800,600)
    x = 250
    for i in range(5):
        new = Circle(Point(400,300),x)
        if i == 0:
            new.setFill("white")
        elif i == 1:
            new.setFill("black")
        elif i == 2:
            new.setFill("blue")
        elif i == 3:
            new.setFill("red")
        elif i == 4:
            new.setFill("yellow")
        new.draw(win)
        x = x - 50
    win.getMouse()
    win.close()

def main4(): # animate this
    win = GraphWin("Winter Scene",800,600)
    win.setCoords(0,0,800,600)
    win.setBackground("lightblue1")
    ground = Rectangle(Point(0,-10),Point(810,200))
    ground.setFill("white")
    ground.draw(win)
    snowman1 = Circle(Point(500,180),40)
    snowman1.setFill("white")
    snowman1.draw(win)
    snowman2 = Circle(Point(500,255),35)
    snowman2.setFill("white")
    snowman2.draw(win)
    snowman3 = Circle(Point(500,320),30)
    snowman3.setFill("white")
    snowman3.draw(win)
    hat1 = Rectangle(Point(470,350),Point(530,360))
    hat1.setFill("magenta4")
    hat1.setWidth(3)
    hat1.draw(win)
    hat2 = Rectangle(Point(485,360),Point(515,400))
    hat2.setFill("magenta4")
    hat2.setWidth(3)
    hat2.draw(win)
    lefteye = Circle(Point(485,330),5)
    lefteye.setFill("black")
    lefteye.draw(win)
    righteye = lefteye.clone()
    righteye.move(30,0)
    righteye.draw(win)
    trunk = Rectangle(Point(200,180),Point(240,350))
    trunk.setFill("brown")
    trunk.draw(win)
    leaves1 = Polygon(Point(125,350),Point(315,350),Point(220,450))
    leaves1.setFill("green4")
    leaves1.draw(win)
    leaves2 = Polygon(Point(135,400),Point(305,400),Point(220,500))
    leaves2.setFill("green4")
    leaves2.draw(win)
    leaves3 = Polygon(Point(145,450),Point(295,450),Point(220,550))
    leaves3.setFill("green4")
    leaves3.draw(win)
    d = {}
    for i in range(500):
        x = random.randint(4,796)
        y = random.randint(4,596)
        d[i] = Circle(Point(x,y),3)
        d[i].setFill("white")
        d[i].setOutline("white")
        d[i].draw(win)
    while True:
        for i in range(500):
            jig = random.randint(-2,2)
            d[i].move(jig,-3)
            center = d[i].getCenter()
            reset = center.getY()
            if reset < 0:
                d[i].move(0,610)
        time.sleep(0.1)
        key = win.checkKey()
        if key == "Return":
            win.close()
            quit()
    win.getMouse()
    win.close()

def main6():
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    # Get principal and interest rate
    win = GraphWin("Investment inputs",320,240)
    win.setCoords(0,0,320,240)
    Text(Point(160,190),"Input the initial principal:").draw(win)
    p = Entry(Point(160,160),10)
    p.draw(win)
    Text(Point(160,110),"Input the annual interest rate (decimal):").draw(win)
    a = Entry(Point(160,80),10)
    a.draw(win)
    win.getMouse()
    principal = eval(p.getText())
    apr = eval(a.getText())
    win.close()
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20, 180), " 2.5K").draw(win)
    Text(Point(20, 130), " 5.0K").draw(win)
    Text(Point(20, 80), " 7.5K").draw(win)
    Text(Point(20, 30), "10.0K").draw(win)
    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

def main8():
    win = GraphWin("Line Segment Information",800,600)
    win.setCoords(0,0,800,600)
    win.setBackground("white")
    while True:
        pt1 = win.getMouse()
        pt1x = pt1.getX()
        pt1y = pt1.getY()
        Point(pt1x,pt1y).draw(win)
        pt2 = win.getMouse()
        pt2x = pt2.getX()
        pt2y = pt2.getY()
        Point(pt2x,pt2y).draw(win)
        line = Line(Point(pt1x,pt1y),Point(pt2x,pt2y))
        line.setWidth(3)
        line.draw(win)
        mid = line.getCenter()
        xmid = mid.getX()
        ymid = mid.getY()
        dot = Circle(Point(xmid,ymid),5)
        dot.setFill("cyan")
        dot.draw(win)
        if pt2x == pt1x:
            pass
        else:
            slope = (pt2y - pt1y) / (pt2x - pt1x)
            length = math.sqrt((pt2x - pt1x)**2 + (pt2y - pt1y)**2)
            print("The slope of the line is",slope)
            print("The length of the line is",length)
        key = win.checkKey()
        if key == "Return" or key == "space":
            win.close()
            quit()

def main10():
    win = GraphWin("Triangle information",800,600)
    win.setCoords(0,0,800,600)
    win.setBackground("white")
    while True:
        pt1 = win.getMouse()
        pt1x = pt1.getX()
        pt1y = pt1.getY()
        Point(pt1x,pt1y).draw(win)
        pt2 = win.getMouse()
        pt2x = pt2.getX()
        pt2y = pt2.getY()
        Point(pt2x,pt2y).draw(win)
        pt3 = win.getMouse()
        pt3x = pt3.getX()
        pt3y = pt3.getY()
        Point(pt3x,pt3y).draw(win)
        a = math.sqrt((pt2x - pt1x)**2 + (pt2y - pt1y)**2)
        b = math.sqrt((pt3x - pt2x)**2 + (pt3y - pt2y)**2)
        c = math.sqrt((pt3x - pt1x)**2 + (pt3y - pt1y)**2)
        triangle = Polygon(Point(pt1x,pt1y),Point(pt2x,pt2y),Point(pt3x,pt3y))
        triangle.setWidth(3)
        triangle.draw(win)
        s = (a + b + c) / 2
        area = math.sqrt(s*(s - a)*(s - b)*(s - c))
        perimeter = a + b + c
        print("The perimeter of the triangle is",perimeter)
        print("The area of the triangle is",area)
        key = win.checkKey()
        if key == "Return" or key == "space":
            win.close()
            quit()



