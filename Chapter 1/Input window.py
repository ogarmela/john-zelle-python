#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brads
#
# Created:     14/09/2017
# Copyright:   (c) brads 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def window():

    run = 0
    win = GraphWin("Calendar Creator",400,500)
    win.setCoords(0.0,0.0,4.0,5.0)

    box = Rectangle(Point(0.1,3.3),Point(3.9,4.15))
    box.setFill("white")
    box.draw(win)
    box2 = box.clone()
    box2.move(0,-1)
    box2.draw(win)
    box3 = box2.clone()
    box3.move(0,-1)
    box3.draw(win)

    Text(Point(2,4),"Enter the month as a number (1-12)").draw(win)
    monthinput = Entry(Point(2,3.5),5)
    monthinput.draw(win)

    Text(Point(2,3),"Enter the starting day of the week as a number (1-7)").draw(win)
    dayinput = Entry(Point(2,2.5),5)
    dayinput.draw(win)

    Text(Point(2,2),"Enter the number of days in the month (28-31)").draw(win)
    numdayinput = Entry(Point(2,1.5),5)
    numdayinput.draw(win)

    button = Rectangle(Point(1.7,0.6),Point(2.3,0.9))
    button.setFill("green")
    button.draw(win)
    create = Text(Point(2,0.75),"Create")
    create.draw(win)

    win.getMouse()
    try:
        month = eval(monthinput.getText())
        day = eval(dayinput.getText())
        numday = eval(numdayinput.getText())
    except SyntaxError:
        run = 1
        win.close()


    win.close()

window()