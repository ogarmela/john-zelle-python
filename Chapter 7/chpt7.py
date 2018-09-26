#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brads
#
# Created:     14/10/2017
# Copyright:   (c) brads 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import math

# True/False:

# 1. True
# 2. False
# 3. True
# 4. False
# 5. True
# 6. True
# 7. False
# 8. False
# 9. True
# 10. False

# Multiple Choice:

# 1. c
# 2. c
# 3. b
# 4. c
# 5. b
# 6. c
# 7. a
# 8. c
# 9. a
# 10. c

# Discussion Questions:

# 1.
# a) A simple decision is a single decision "if statement" which, if true,
# exectues the code in the body of the statement.
# b) A two-way decision is a decision statement that checks if the first
# "if" is true, and if not, executes the other statement. Usually if-else.
# c) A multi-way decision checks each statement in the order they are produced.
# Once a true statement is found, it executes that body, and skips to after
# the decision structure.

# 2.
# a)
# Trees
# Larch
# Done
# b)
# Trees
# Chestnut
# Done
# c)
# Spam Please!
# Done
# d)
# Cheese Shoppe
# Cheddar
# Done
# e)
# It's a late parrot!
# Done
# f)
# Cheese Shoppe
# Cheddar
# Done

# 3.
# Exception-handling using try/except is similar to ordinary decision structures
# because they follow the same structure, where if something rings True (or in this case, there is no error),
# the Try: body is executed, and if not, the except is executed, like an if-else.
# However, they differ in the way that the try body will always attempt to execute
# and will only skip the rest of the body if a Python error is presented
# that matches with the except statement.

# Programming Exercises

def getGrade(score):
    if score == 0 or score == 1:
        grade = "F"
    elif score == 2:
        grade = "D"
    elif score == 3:
        grade = "C"
    elif score == 4:
        grade = "B"
    elif score == 5:
        grade = "A"
    else:
        print("You entered an invalid score.")
        quit()
    return grade

def main2():
    print("This program calculates the score of a 5-point quiz.")
    try:
        score = eval(input("Enter a quiz score on the scale of 0-5."))
    except NameError:
        print("You didn't enter a number. Quitting program...")
        quit()
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input Error. Program quit.")
        quit()
    grade = getGrade(score)
    print("Your grade is {0}".format(grade))

#--------------------------------------------------------------------------------------------------------------------------------------------------

def statusCalc(cred):
    if cred < 7:
        stat = "Freshman"
    elif cred >= 7 and cred < 16:
        stat = "Sophomore"
    elif cred >= 16 and cred < 26:
        stat = "Junior"
    else:
        stat = "Senior"
    return stat

def main4():
    print("this program displays your college classification.")
    try:
        cred = eval(input("Enter the number of credits earned."))
        math.sqrt(cred)
    except NameError:
        print("You didn't enter a number. Program quit.")
        quit()
    except ValueError:
        print("Negative numbers not allowed. Program quit.")
        quit()
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input error. Program quit.")
        quit()
    stat = statusCalc(cred)
    print("Your class standing is {0}".format(stat))

#--------------------------------------------------------------------------------------------------------------------------------------------------

def ticketValue(limit,clock):
    if clock <= limit:
        fine = 0
    elif clock <= 90:
        fine = 50 + (clock - limit) * 5
    else:
        fine = 200 + (clock - limit) * 5
    return fine

def main6():
    print("This program calculates the ticket fine policy in Podunksville.")
    try:
        limit, clock = eval(input("Enter the speed limit, then the clocked speed. (mph):"))
        math.sqrt(limit)
        math.sqrt(clock)
    except NameError:
        print("You didn't enter a number. Program quit.")
        quit()
    except ValueError:
        print("Negative numbers not allowed. Program quit.")
        quit()
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input error. Program quit.")
        quit()
    fine = ticketValue(limit,clock)
    if fine == 0:
        print("Your speed ({0}mph) was legal with respect to a speed limit of {1}mph".format(clock,limit))
    else:
        print("You earned yourself a fine of ${0} by driving {1}mph over the speed limit.".format(fine,clock-limit))

#--------------------------------------------------------------------------------------------------------------------------------------------------

def authority(age,citizen):
    if age >= 30 and citizen >= 9:
        senator = True
        representative = True
    elif age >= 25 and citizen >= 7:
        senator = False
        representative = True
    else:
        senator = False
        representative = False
    return senator, representative

def main8():
    print("This program determines if you are eligible to be a US senator and/or representative.")
    try:
        age, citizen = eval(input("Enter your age, then the number of years you have been a US citizen."))
        math.sqrt(age)
        math.sqrt(citizen)
    except NameError:
        print("You didn't enter a number. Program quit.")
        quit()
    except ValueError:
        print("Negative numbers not allowed. Program quit.")
        quit()
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input error. Program quit.")
        quit()
    senator, representative = authority(age, citizen)
    if senator == True and representative == True:
        print("You are eligible to be a senator and representative.")
    elif senator == False and representative == True:
        print("You are eligible to be a representative but not a senator.")
    else:
        print("You are ineligible to be a senator or representative.")

#--------------------------------------------------------------------------------------------------------------------------------------------------

def findEaster(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    month = "March"
    day = 22
    easter = day + d + e
    if easter > 31:
        month = "April"
        easter = easter - 31
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        easter = easter - 7
    return easter, month

def main10():
    print("This program finds the date of Easter in a given year (range 1900-2099).")
    try:
        year = eval(input("Enter a year in the range 1900-2099: "))
    except NameError:
        print("You didn't enter a number. Program quit.")
        quit()
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input error. Program quit.")
        quit()
    if year < 1900 or year > 2099:
        print("Input year outside of range (1900-2099). Program quit.")
        quit()
    easter, month = findEaster(year)
    print("The date of Easter in {0} is {1} {2}".format(year, month, easter))

#--------------------------------------------------------------------------------------------------------------------------------------------------

def getDateValue(date):
    month = date.split("/")[0]
    day = date.split("/")[1]
    year = date.split("/")[2]
    month = int(month)
    day = int(day)
    year = int(year)
    return month, day, year

def getLeapYear(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap

def main12():
    print("This program accepts a date in the form month/day/year and outputs\n"
    "whether the date is valid or invalid.\n")
    try:
        date = input("Enter a date in the form mm/dd/yyyy.")
    except KeyboardInterrupt:
        print("Program quit.")
        quit()
    except:
        print("Input error. Program quit.")
        quit()
    try:
        month, day, year = getDateValue(date)
    except:
        print("Date is invalid. (Not in the correct form: mm/dd/yyyy)")
        quit()
    leap = getLeapYear(year)
    maxMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap == True:
        maxMonth[1] = 29
    if month > 0 and month <= 12 and day <= maxMonth[month - 1] and day > 0:
        print("The date {0} is valid.".format(date))
    else:
        print("The date {0} is invalid.".format(date))

#--------------------------------------------------------------------------------------------------------------------------------------------------

def draw_Window(radius, yint):
    win = GraphWin("Circle Intersection",600,600)
    win.setCoords(-10,-10,10,10)
    circ = Circle(Point(0,0),radius)
    circ.setFill("magenta3")
    circ.draw(win)
    line = Line(Point(-10,yint),Point(10,yint))
    line.setFill("blue3")
    line.draw(win)
    return win

def decision(win, radius, yint):
    if radius >= yint:
        x1 = math.sqrt(radius**2 - yint**2)
        x2 = -(math.sqrt(radius**2 - yint**2))
        drawx1 = Circle(Point(x1,yint),0.15)
        drawx1.setFill("red")
        drawx1.draw(win)
        drawx2 = Circle(Point(x2,yint),0.15)
        drawx2.setFill("red")
        drawx2.draw(win)
        Text(Point(-5,-9),"The x-intercepts are {0:.2f} and {1:.2f}".format(x1,x2)).draw(win)
    else:
        Text(Point(-5,-9),"There are no x-intercepts.").draw(win)

def main14():
    print("This program computes the intersection of a circle with a horizontal\nline and displays the information textually and graphically.")
    try:
        radius, yint = eval(input("Enter the radius of the circle (positive), then the y-intercept of the horizontal line:\n"
        "(The coordinate system has max values from -10 to +10)"))
        math.sqrt(radius)
    except NameError:
        print("\nYou didn't enter a number. Program quit.")
        quit()
    except ValueError:
        print("\nThe radius cannot be negative. Program quit.")
        quit()
    except KeyboardInterrupt:
        print("\nProgram quit.")
        quit()
    except:
        print("\nInput error. Program quit.")
        quit()
    if radius <-10 or radius >10 or yint <-10 or yint >10:
        print("\nInput values outside the coordinate range (max values -10 to +10). Program terminated.")
        quit()
    win = draw_Window(radius, yint)
    decision(win, radius, yint)
    Text(Point(5,-9),"Click to close").draw(win)
    Line(Point(-10,0),Point(10,0)).draw(win)
    Line(Point(0,-10),Point(0,10)).draw(win)
    win.getMouse()
    win.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------

def createWindow():
    win = GraphWin("Archery Target",800,600)
    win.setCoords(0,0,800,600)
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
    Text(Point(400,575),"Click on 5 points to shoot five arrows!").draw(win)
    Text(Point(75,540),"Yellow = 9 points\nRed = 7 points   \nBlue = 5 points   \nBlack = 3 points \nWhite = 1 point   ").draw(win)
    score = 0
    score_text = Text(Point(725,575),"Your score is:\n{0}".format(score))
    score_text.draw(win)
    pop_up = Text(Point(150,50),"")
    pop_up.draw(win)
    return win, score, score_text, pop_up

def shootArrow(win):
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    arrowhead = Polygon(Point(x,y),Point(x-10,y-10),Point(x+10,y-10))
    arrowhead.setFill("grey")
    arrowhead.setOutline("grey")
    arrowhead.draw(win)
    shaft = Line(Point(x, y-10),Point(x, y-50))
    shaft.setWidth(4)
    shaft.setFill("brown")
    shaft.draw(win)
    fletching = Polygon(Point(x, y-50), Point(x-10, y-55), Point(x-10, y-70), Point(x, y-67.5), Point(x+10, y-70), Point(x+10, y-55))
    fletching.setFill("white")
    fletching.draw(win)
    return x, y

def keepScore(x, y, score, score_text, pop_up):
    if (x - 400)**2 + (y - 300)**2 < 50**2:
        score = score + 9
        pop_up.setText("BULLS-EYE! You scored 9 points!")
    elif (x - 400)**2 + (y - 300)**2 < 100**2:
        score = score + 7
        pop_up.setText("Red! You scored 7 points!")
    elif (x - 400)**2 + (y - 300)**2 < 150**2:
        score = score + 5
        pop_up.setText("Blue! You scored 5 points!")
    elif (x - 400)**2 + (y - 300)**2 < 200**2:
        score = score + 3
        pop_up.setText("Black! You scored 3 points!")
    elif (x - 400)**2 + (y - 300)**2 < 250**2:
        score = score + 1
        pop_up.setText("White! You scored 1 point.")
    else:
        pop_up.setText("HAH! that's a zero!")
    score_text.setText("Your score is:\n{0}".format(score))
    return score

def main16():
    win, score, score_text, pop_up = createWindow()
    for i in range(5):
        try:
            x, y = shootArrow(win)
        except:
            print("Program quit.")
            quit()
        score = keepScore(x, y, score, score_text, pop_up)
    Text(Point(400,25),"Click to close").draw(win)
    try:
        win.getMouse()
    except:
        print("Program quit.")
        quit()
    win.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------

def createWindow2():
    win = GraphWin("Line Segment Information",800,600)
    win.setCoords(0,0,800,600)
    win.setBackground("white")
    Text(Point(400,575),"Click on two points to create a line.").draw(win)
    Text(Point(400,50),"Press Enter or space and finish creating the line to quit.").draw(win)
    Text(Point(400,25),"(WARNING) This program requires John Zelle's newest graphics module with operation 'checkKey'.").draw(win)
    return win

def lineCreator(win, length_text, slope_text):
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
    length = math.sqrt((pt2x - pt1x)**2 + (pt2y - pt1y)**2)
    length_text.setText("The length is: {0:.2f}".format(length))
    if pt2x == pt1x:
        slope_text.setText("The slope is: unlimited")
    else:
        slope = (pt2y - pt1y) / (pt2x - pt1x)
        slope_text.setText("The slope is: {0:.2f}".format(slope))

def checkExit(win):
    key = win.checkKey()
    if key == "Return" or key == "space":
        win.close()
        quit()

def main18(): #Take a favorite problem from a previous chapter and make it robust
    win = createWindow2()
    slope = 0
    length = 0
    slope_text = Text(Point(85,350),"The slope is: {0:.2f}".format(slope))
    slope_text.draw(win)
    length_text = Text(Point(85,325),"The length is: {0:.2f}".format(length))
    length_text.draw(win)
    while True:
        try:
            lineCreator(win, length_text, slope_text)
            checkExit(win)
        except:
            print("Program terminated.")
            quit()



