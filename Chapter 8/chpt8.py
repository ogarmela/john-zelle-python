#-------------------------------------------------------------------------------
# Name:        chpt8
# Purpose:
#
# Author:      brads
#
# Created:     17/10/2017
# Copyright:   (c) brads 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
from graphics import *
import os

# True/False:

# 1. False
# 2. True
# 3. False
# 4. True
# 5. False
# 6. False
# 7. True
# 8. True
# 9. False
# 10. True

# a or (b and c) == (a or b) and (a or c)
# a and (b or c) == (a and b) or (a and c)
# not(a or b) == (not a) and (not b)
# not(a and b) == (not a) or (not b)

# Multiple Choice:
# 1. a
# 2. c
# 3. d
# 4. c
# 5. c
# 6. c
# 7. d
# 8. b
# 9. c
# 10. a

# Discussion:

# Programming Exercises:

def windChill(t,v):
    chill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    return chill

def main2():
    Vwind = 5
    print("This chart represents the value of wind chill based on the wind speed and temperature.\n")
    print("       |  -20F  |  -10F  |   0F   |  10F   |  20F   |  30F   |  40F   |  50F   |  60F   |")
    print("-----------------------------------------------------------------------------------------")
    x = 0
    print(" {0:>2}mph | {1:>6.2f} | {2:>6.2f} | {3:>6.2f} | {4:>6.2f} | {5:>6.2f} | {6:>6.2f} | {7:>6.2f} | {8:>6.2f} | {9:>6.2f} |".format(x,-20,-10,0,10,20,30,40,50,60))
    d = {}
    i = 0
    while i != 10:
        i = i + 1
        Temp = -20
        x = 1
        while x != 10:
            chill = windChill(Temp, Vwind)
            d["x{0}".format(x)] = chill
            Temp = Temp + 10
            x = x + 1
        print(" {0:>2}mph | {1:>6.2f} | {2:>6.2f} | {3:>6.2f} | {4:>6.2f} | {5:>6.2f} | {6:>6.2f} | {7:>6.2f} | {8:>6.2f} | {9:6.2f} |".format(Vwind,d["x1"],d["x2"],d["x3"],d["x4"],d["x5"],d["x6"],d["x7"],d["x8"],d["x9"]))
        Vwind = Vwind + 5

#-------------------------------------------------------------------------------

def validInput(num):
    if num > 0:
        return True
    else:
        return False

def syr(x):
    if x % 2 == 0:
        return x//2
    else:
        return 3*x + 1

def main4():
    print("This program takes a natural number (>) and does int operations on it to reduce it to 1.")
    while True:
        try:
            num = eval(input("Enter the starting natural number (>2):"))
            if validInput(num) == True:
                break
            print("Input error. Enter a number greater than 2.")
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except SyntaxError:
            print("Your input was in the wrong form.")
        except NameError:
            print("You didn't enter a number.")
        except:
            print("Incorrent input.")
    if num != 1:
        print("{0}".format(num), end = ", ")
    else:
        print("{0}".format(num), end = "")
    while num != 1:
        num = syr(num)
        if num !=1:
            print("{0}".format(num), end = ", ")
        else:
            print("{0}".format(num), end = "")

#-------------------------------------------------------------------------------

def prime(num):
    count = int(math.sqrt(num))
    while count >= 2:
        if (num % count) != 0:
            count = count - 1
        else:
            return False
    return True

def main6():
    num = 0
    while num <= 2:
        Error = False
        try:
            num = eval(input("Enter a positive whole number (>2) to determine if it and any numbers less than it is are prime numbers."))
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except SyntaxError:
            print("Your input was in the wrong form.")
            Error = True
        except NameError:
            print("You didn't enter a number.")
            Error = True
        except:
            print("Incorrent input.")
            Error = True
        if num <= 2 and Error == False:
            print("Incorrect input. Enter a number greater than 2.")
    print("Prime numbers equal to or below {0}:".format(num))
    while num > 2:
        if prime(num) == True:
            print("{0}".format(num), end = ", ")
        num = num - 1
    if num == 2:
        print("{0}".format(num))

#-------------------------------------------------------------------------------

def calcGCD(n,m):
    while m != 0:
        n, m = m, n%m
    return n

def main8():
    print("This program takes two numbers and finds their greatest common divisor.")
    while True:
        try:
            n1, n2 = eval(input("Enter two numbers separated by a comma:"))
            n = calcGCD(n1,n2)
            print("The GCD (greatest common divisor) of {0} and {1} is: {2}".format(n1, n2, n))
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except NameError:
            print("You didn't enter two numbers.")
        except ValueError:
            print("You entered too many values (only 2 allowed).")
        except:
            print("Incorrect input (enter two values, seperated by a comma).")
        else: break

#-------------------------------------------------------------------------------

def extract_num(line, start_miles, m_total, g_total):
    miles, gallons = line.split(" ")
    miles = eval(miles)
    gallons = eval(gallons)
    miles = miles - start_miles
    start_miles = start_miles + miles
    m_total = m_total + miles
    g_total = g_total + gallons
    return miles, gallons, start_miles, m_total, g_total

def main10():
    print("This program outputs information on the fuel efficiency achieved on a multi-leg journey based on odometer values and fuel usage.\nInput is read from a file (units are in miles and gallons -> MPG).")
    print("Proper file setup:\n(initial odometer reading)\n(new odometer reading)[space](gallons used on current leg).\n(new odometer reading)[space](gallons used on current leg).\netc...\n")
    while True:
        try:
            file = open(input("Input the location of the file to read from:"), "r")
            line = file.readline()
            start_miles = eval(line)
            count = 0
            m_total = 0
            g_total = 0
            line = file.readline()
            while line != "":
                count = count + 1
                miles, gallons, start_miles, m_total, g_total = extract_num(line, start_miles, m_total, g_total)
                mpg = miles / gallons
                print("The fuel efficiency for leg {0} is: {1:>4.1f} mpg".format(count, mpg))
                line = file.readline()
            total_mpg = m_total / g_total
            print("The total fuel efficiency of the trip is: {0:0.1f} mpg".format(total_mpg))
            file.close()
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except IOError:
            print("No such file or directory found.")
        except:
            print("File content error; check file setup.")
        else: break


#-------------------------------------------------------------------------------

def get_days(line,CDD,HDD):
    line = eval(line)
    if line < 60:
        HDD = HDD + (60 - line)
    elif line > 80:
        CDD = CDD + (line - 80)
    return CDD, HDD

def main12():
    print("This program calculates the running total of cooling and heating degree-days from a file.\nThe file should contain temperature values (in fahrenheit), one per each line.\n")
    while True:
        try:
            file = open(input("Enter the file to be read from:"),"r")
            CDD = 0
            HDD = 0
            count = 0
            line = file.readline()
            while line != "":
                CDD, HDD = get_days(line,CDD,HDD)
                count = count + 1
                line = file.readline()
            print("The total number of days is: {0}".format(count))
            print("The total of cooling degree days is: {0}".format(CDD))
            print("The total of heating degree days is: {0}".format(HDD))
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except IOError:
            print("No such file or directory found.")
        except:
            print("File setup error.")
        else: break

#-------------------------------------------------------------------------------

def create_window():
    getpic = input("Enter the location of the image you want to convert:")
    try:
        open(getpic)
    except IOError:
        1/0
    picture = Image(Point(0,0),getpic)
    picture.move(picture.getWidth()/2,picture.getHeight()/2)
    win = GraphWin("Grayscale Converter",picture.getWidth(),picture.getHeight() + 50)
    win.setCoords(0,0,picture.getWidth(),picture.getHeight() + 50)
    win.setBackground("black")
    instruct = Text(Point(picture.getWidth()/2, picture.getHeight() + 25), "Click to convert to grayscale (may take a while)")
    instruct.setTextColor("white")
    instruct.setSize(16)
    instruct.draw(win)
    picture.draw(win)
    return win, picture, instruct

def convert_to_grayscale(picture):
    y = 0
    while y < picture.getHeight():
        x = 0
        while x < picture.getWidth():
            r, g, b = picture.getPixel(x,y)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            picture.setPixel(x,y,color_rgb(brightness,brightness,brightness))
            x = x + 1
        y = y + 1

def main14():
    print("This program takes any picture as input, displays it, then converts it to grayscale on the click of the mouse.")
    Error = False
    while True:
        try:
            win, picture, instruct = create_window()
            win.getMouse()
            convert_to_grayscale(picture)
            instruct.setText("Click again to save the file.")
            win.getMouse()
            win.close()
            try:
                savename = input("Save file as:")
            except KeyboardInterrupt:
                print("Program quit.")
                Error = True
                win.close()
                quit()
            if savename.count(".gif") == 0 and savename.count(".ppm") == 0:
                math.sqrt(-1)
            else:
                picture.save(savename)
            win.close()
        except KeyboardInterrupt:
            print("Program quit.")
            quit()
        except GraphicsError:
            print("Program quit.")
            quit()
        except ZeroDivisionError:
            print("File not found.")
        except ValueError:
            print("File format incorrect.")
            win.close()
            quit()
        except:
            if Error == False:
                print("Something went wrong.")
            quit()
        else: break


