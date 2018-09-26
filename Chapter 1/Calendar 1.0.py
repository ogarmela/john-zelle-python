#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     13/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import*


def calendar():

# input

    lol = eval(input.getText())
    month = eval(input("Enter the month as a number (1-12)."))
    if month < 1:
        month = 1
        print("ERROR!")
        print("Month value out of range, set to January. Correct range is 1-12")
    if month >12:
        month = 12
        print("ERROR!")
        print("Month value out of range, set to December. Correct range is 1-12")
    day = eval(input("Enter the starting day of the week as a number (1-7) (1 for Sunday, 7 for saturday)."))
    if day < 1:
        day = 1
        print("ERROR!")
        print("Starting day value out of range, set to Sunday. Correct range is 1-7")
    if day >7:
        day = 7
        print("ERROR!")
        print("Starting day value out of range, set to Saturday. Correct range is 1-7")
    numday = eval(input("Enter the number of days in the month as a number (28-31)."))
    if numday < 28:
        numday = 28
        print("ERROR!")
        print("number of days value out of range, set to 28. Correct range is 28-31.")
    if numday >31:
        numday = 31
        print("ERROR!")
        print("number of days value out of range, set to 31. Correct range is 28-31.")

    monthstring = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    monthstring = monthstring[month-1]
#    print(monthstring)





# Rows

    if day >= 6:
        win = GraphWin("Calendar", 700,700)
    else:
        win = GraphWin("Calendar", 700,600)
    background = Rectangle(Point(0,50),Point(700,700))
    background.setFill("white")
    background.draw(win)
    line0 = Line(Point(0,50),Point(700,50))
    line0.draw(win)
    line1 = Line(Point(0,100),Point(700,100))
    line1.draw(win)
    line2 = Line(Point(0,200),Point(700,200))
    line2.draw(win)
    line3 = Line(Point(0,300),Point(700,300))
    line3.draw(win)
    line4 = Line(Point(0,400),Point(700,400))
    line4.draw(win)
    line5 = Line(Point(0,500),Point(700,500))
    line5.draw(win)
    line6 = Line(Point(0,600),Point(700,600))
    line6.draw(win)

# Columns

    line7 = Line(Point(2,50),Point(2,700))
    line7.draw(win)
    line8 = Line(Point(100,50),Point(100,700))
    line8.draw(win)
    line9 = Line(Point(200,50),Point(200,700))
    line9.draw(win)
    line10 = Line(Point(300,50),Point(300,700))
    line10.draw(win)
    line11 = Line(Point(400,50),Point(400,700))
    line11.draw(win)
    line12 = Line(Point(500,50),Point(500,700))
    line12.draw(win)
    line13 = Line(Point(600,50),Point(600,700))
    line13.draw(win)
    line14 = Line(Point(700,50),Point(700,700))
    line14.draw(win)

# Month

    title = Text(Point(350,25),monthstring)
    title.setSize(30)
    title.setFace("courier")
    title.setTextColor("red")
    title.setStyle("italic")
    title.draw(win)

# Days of the week

    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    daysx = 0
    x = 50
    for i in range(7):
        date = days[daysx]
#        print(date)
#        print(daysx)
        daytext = Text(Point(x,75),date)
        daytext.setStyle("bold")
        if date == "Sunday":
            daytext.setTextColor("red")
        if date == "Saturday":
            daytext.setTextColor("blue")
        daytext.draw(win)
        daysx = daysx + 1
        x = x + 100

# Starting day

    xpos = day * 100 - 50
    ypos = 150
    NUMBERZ = 0

# Day loop

    for i in range(numday):
        NUMBERZ = NUMBERZ + 1
        xtext = Text(Point(xpos,ypos),NUMBERZ)
        xtext.setSize(25)
        xtext.setFace("helvetica")
        if xpos == 50:
            xtext.setTextColor("red")
        if xpos == 650:
            xtext.setTextColor("blue")
        xtext.draw(win)
        xpos = xpos + 100
        if xpos>700:
            ypos = ypos + 100
            xpos = 50





    win.getMouse()
    win.close()

calendar()

