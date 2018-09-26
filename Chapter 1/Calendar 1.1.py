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

# Input screen

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
    try: # Error handling, otherwise if no numbers are inputted it crashes and displays an error
        month = eval(monthinput.getText())
        day = eval(dayinput.getText())
        numday = eval(numdayinput.getText())
    except SyntaxError:
        run = 1
    win.close()

    if run == 0: #does not create the calendar if not all numbers were inputted

    # error reporting and fixing

        if month < 1:
            month = 1
            print("ERROR!")
            print("Month value out of range, set to January. Correct range is 1-12")
        if month >12:
            month = 12
            print("ERROR!")
            print("Month value out of range, set to December. Correct range is 1-12")
        if day < 1:
            day = 1
            print("ERROR!")
            print("Starting day value out of range, set to Sunday. Correct range is 1-7")
        if day >7:
            day = 7
            print("ERROR!")
            print("Starting day value out of range, set to Saturday. Correct range is 1-7")
        if numday < 28:
            numday = 28
            print("ERROR!")
            print("number of days value out of range, set to 28. Correct range is 28-31.")
        if numday >31:
            numday = 31
            print("ERROR!")
            print("number of days value out of range, set to 31. Correct range is 28-31.")

        monthstring = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        monthstring = monthstring[month-1] # selects string from list based on the number the user inputted

        if day >= 6:
            win = GraphWin("Calendar", 700,700)
        else:
            win = GraphWin("Calendar", 700,600)

    # Rows

        background = Rectangle(Point(0,50),Point(700,700))
        background.setFill("white")
        background.draw(win)

        tline = Line(Point(0,50),Point(700,50))
        tline.draw(win)
        xline = Line(Point(0,100),Point(700,100))
        xline.draw(win)
        repeat = 100
        for i in range(5):
            newline = xline.clone()
            newline.move(0,repeat)
            newline.draw(win)
            repeat = repeat + 100

    # Columns

        yline = Line(Point(2,50),Point(2,700))
        yline.draw(win)
        repeat = 100
        for i in range(7):
            newline = yline.clone()
            newline.move(repeat,0)
            newline.draw(win)
            repeat = repeat + 100

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

