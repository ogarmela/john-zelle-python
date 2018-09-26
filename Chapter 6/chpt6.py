#-------------------------------------------------------------------------------
# Name:        Chapter 6
# Purpose:
#
# Author:      brads
#
# Created:     06/10/2017
# Copyright:   (c) brads 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# True/False

# 1. False
# 2. False
# 3. True
# 4. True
# 5. False
# 6. False
# 7. False
# 8. True
# 9. True
# 10. False

# Multiple Choice

# 1. b
# 2. a
# 3. a
# 4. b
# 5. d
# 6. a
# 7. d
# 8. a
# 9. d
# 10. a

# Discussion Questions

# 1.
# Two motivations to define functions in your programs is to make the code more
# modular, and to make it easier to read.
# 2.
# Yes, these programs fit this model. This is because when the computer reaches
# the line of code with the function in it, it just calls the function and
# goes through that first. If it didn't do this, the computer would be skipping
# lines of code.
# 3.
# a)
# The purpose of parameters is to accept a value from the calling function
# so that the nested function can use those parameters.
# b)
# A formal parameter is what is defined in the function and is a placeholder for
# the actual parameters. An actual parameter is one from the main function
# that gives its value to the formal parameter.
# c)
# When using parameters in a function, the syntax is identical to using
# ordinary variables because these parameters need to take the value of a
# varaible.
# 4.
# a)
# A program provides input to one of its functions by inputting one of the
# variables of the main function into the function's parameters.
# b)
# The function provides output in the way of returning a value that is now
# equal to what the function does. Hence, usually functions are called in
# expressions.
# 5.
# a)
# This function returns the cube of the value in the parameter.
# b)
# def main():
#   y = 4
#   result = cube(y) ## Function is already defined
#   print(result)
# c)
# Cube does not change the value of answer to 27. answer stays as 4.
# cube(3) only applies to the variable result and that's why answer does not change.

# Programming Exercises

def antsMarch(num,lyric):
    print("The ants go marching {0} by {0} hurrah! hurrah!".format(num))
    print("The ants go marching {0} by {0} hurrah! hurrah!".format(num))
    print("The ants go marching {0} by {0}".format(num))
    print("The little one stops to {0}".format(lyric))
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def main2():
    for i in range(10):
        list = ["suck his thumb","tie his shoe","climb a tree","shut the door","take a dive",
        "pick up sticks","pray to heaven","roller skate","check the time","shout 'The End'"]
        lyric = list[i]
        antsMarch(i+1,lyric)

#--------------------------------------------------------------------------------------------------

def sumN(n):
    sum = 0
    for i in range(n):
        sum = sum + (i + 1)
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(n):
        sum = sum + ((i + 1) ** 3)
    return sum

def main4():
    n = eval(input("Enter the nth term of the first natural numbers."))
    print("The sum of these numbers is: {0}.\n".format(sumN(n)) +
          "The sum of the cube of these numbers is: {0}.".format(str(sumNCubes(n))))

#--------------------------------------------------------------------------------------------------

def areaTriangle(p1,p2,p3):
    a = math.sqrt(abs((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2))
    b = math.sqrt(abs((p3.getX() - p2.getX())**2 + (p3.getY() - p2.getY())**2))
    c = math.sqrt(abs((p1.getX() - p3.getX())**2 + (p1.getY() - p1.getY())**2))
    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    return area

def main6():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    # Calculate the area of the triangle
    area = areaTriangle(p1,p2,p3)
    message.setText("The area is: {0:0.2f}".format(area))
    # Wait for another click to exit
    win.getMouse()
    win.close()

#--------------------------------------------------------------------------------------------------

def nextGuess(x,guess,numG):
    nextG = 0
    for i in range(numG):
        guess = (guess + (x/guess)) / 2
    return guess

def main8():
    x,guess,numG = eval(input("Enter the number to square root, \nyour guess,"
    "\nthen the number of guesses to improve the value."))
    finalguess = nextGuess(x,guess,numG)
    print("The final guess is {0}"
    "\nThe real value was {1}"
    "\nThe difference between them is {2}".format(finalguess,math.sqrt(x),abs(finalguess-math.sqrt(x))))

#--------------------------------------------------------------------------------------------------

def acronym(phrase):
    acr = ""
    for word in phrase.split():
        acr = acr + word[0]
    acr = acr.upper()
    return acr

def main10():
    phrase = input("Enter a phrase to get an acronym: ")
    acr = acronym(phrase)
    print("The acronym of '{0}' is {1}".format(phrase,acr))

#--------------------------------------------------------------------------------------------------

def squareEach(nums):
    nums = list(nums)
    alist = []
    for i in nums:
        alist.append(i ** 2)
    return alist

def sumList(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def toNumber(strList):
    newList = []
    strNum = []
    for i in strList:
        for x in i.split(","):
            if x == "":
                break
            x = eval(x)
            newList.append(x)
    return newList

def main14():
    print("This program computes the sum of the square of numbers read from a file.")
    inFile = open(input("Enter a file of numbers to be read from:"))
    file = inFile.readlines()
    newfile = []
    listNum = []
    for i in file:
        if i[-1] == "\n":
            newfile.append(i[:-1])
        else:
            newfile.append(i)
    floatList = toNumber(newfile)
    squareList = squareEach(floatList)
    sum = sumList(squareList)
    print("The sum of the squares in this file is: {0}".format(sum))
    inFile.close()

#--------------------------------------------------------------------------------------------------

def drawFace(center, size, win):
    lxcenter = center.getX()
    lycenter = center.getY()
    outface = Circle(center, size * 10)
    outface.setFill("yellow")
    outface.draw(win)
    lefteye = Circle(Point(lxcenter - size*4, lycenter + size*4), size * 2)
    lefteye.setFill("white")
    lefteye.draw(win)
    righteye = lefteye.clone()
    righteye.move(size*8, 0)
    righteye.draw(win)
    lpupil = Circle(Point(lxcenter - size*4, lycenter + size*4), size*0.5)
    lpupil.setFill("lightblue")
    lpupil.draw(win)
    rpupil = lpupil.clone()
    rpupil.move(size*8,0)
    rpupil.draw(win)
    mouth1 = Oval(Point(lxcenter - size*6, lycenter - size*8), Point(lxcenter + size*6, lycenter + size*1.5))
    mouth1.setWidth(2)
    mouth1.setFill("black")
    mouth1.draw(win)
    mouthcenter = mouth1.getCenter()
    mouthcx = mouthcenter.getX()
    mouthcy = mouthcenter.getY()
    cutmouth = Rectangle(Point(mouthcx - size*6, mouthcy), Point(mouthcx + size*6, mouthcy + size*4.91))
    cutmouth.setOutline("yellow")
    cutmouth.setFill("yellow")
    cutmouth.draw(win)
    straightmouth = Line(Point(mouthcx - size*6, mouthcy), Point(mouthcx + size*6, mouthcy))
    straightmouth.setWidth(2)
    straightmouth.draw(win)

def getSize(win):
    pt = win.getMouse()
    xcenter = pt.getX()
    ycenter = pt.getY()
    center = Point(xcenter, ycenter)
    drawcenter = Circle(center, 4)
    drawcenter.setFill("lightblue")
    drawcenter.draw(win)
    pt2 = win.getMouse()
    xoutside = pt2.getX()
    youtside = pt2.getY()
    dx = abs(xoutside - xcenter)
    dy = abs(youtside - ycenter)
    size = math.sqrt(dx**2 + dy**2) / 10
    return center, size

def main16():
    getimage = input("Enter the image name to load it: ")
    image = Image(Point(0, 0), getimage)
    ximage = image.getWidth()
    yimage = image.getHeight()
    win = GraphWin("Photo Anonymizer: click the center of the face, then an edge to draw a face", ximage, yimage)
    win.setCoords(0, 0, ximage, yimage)
    image.move(ximage/2, yimage/2)
    image.draw(win)
    facenum = eval(input("Enter the number of faces to be blocked: "))
    for i in range(facenum):
        center, size = getSize(win)
        drawFace(center, size, win)
    win.getMouse()
    win.close()

#--------------The_Online_Version------------------------------------------------------------------

def moveTo(shape, newCenter):
    center = shape.getCenter()
    centerx = center.getX()
    centery = center.getY()
    newCenterx = newCenter.getX()
    newCentery = newCenter.getY()
    shape.move(newCenterx - centerx, newCentery - centery)
    return shape

def main16old(): #The online version
    win = GraphWin("Circle Drawer",800,600)
    win.setCoords(0,0,800,600)
    Text(Point(400,550),"Click on a point to move the circle there.").draw(win)
    shape = Circle(Point(400,300),30)
    shape.setFill("red2")
    shape.draw(win)
    for i in range(10):
        pt = win.getMouse()
        shape = moveTo(shape, pt)
    Text(Point(400,50),"Click once to exit.").draw(win)
    win.getMouse()
    win.close()


