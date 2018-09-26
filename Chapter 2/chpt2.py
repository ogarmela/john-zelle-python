#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     18/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Chapter 2

# Discussion Questions

# 1. The six steps in the software development process are:
# Analyzing the problem
# Determing what your program will do
# Creating the structure of your program
# Implementing the structure into the programming language
# Debugging the program
# Continuously update the program

# 3. A definite loop will execute a definite number of times.
# A counted loop is built using a python for statement. for i in range(10): is a counted loop.
# For loops follow this general form: for <var> in <sequence>:

# 4. a)
# 1
# 1
# 1
# 1
# 1
#   b)
# 3 1 4 1 5
#   c)
# Hello
# Hello
# Hello
# Hello
#   d)
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2

# 5. It's a good idea to first write out an algorithim in pseudocode
# rather than jumping immediately to python code because it allows you to
# put down all your ideas about what you want to program to do without worrying
# about  the rules of Python's syntax.

# 6. The sep parameter controls the seperation between multiple strings in a print statement.
# Normally, sep = " ", so that a space is printed between two strings
# print("Hello", "world")
# Hello world
# print("Hello", "world", sep = "")
# Helloworld

# 7.
# It will print start, then end on a new line. Nothing in between
# because the range parameter is set to 0.

# Programming Excercises (2,4,5,7,9)

def main2():
    print("This program computes the average of three exam scores.")
    score1,score2,score3 = eval(input("Enter three scores separated by a comma."))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average)

def main4():
    print("Celsius","Fahrenheit",sep = "     ")
    celsius = 0
    for i in range(11):
        fahrenheit = (9/5 * celsius + 32)
        fahrenheit = str(fahrenheit)
        print(celsius, fahrenheit.rjust(12), sep = "     ")
        fahrenheit = float(fahrenheit)
        celsius = celsius + 10

def main5():
    print("This program calculates the future value")
    print("of your money after the amount of years that were invested.")
    principal = eval(input("Enter the initial principal"))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for your investment."))
    for i in range(years):
        principal = principal * (1 + apr/100)
    print("The value in",years,"years is:",principal)

def main7():
    print("This program calculates the future value")
    print("of your money after 10 years of compound interest.")
    principal = eval(input("Enter the initial principal"))
    apr = eval(input("Enter the annual interest rate: "))
    compound = eval(input("Enter the amount of compounding periods. (12 = monthly, 4 = quarterly)"))
    for i in range(10):
        for i in range(compound):
            principal = principal * (1 + (apr/100/compound))
    print("The value in 10 years is:",round(principal,2))

def main9():
    print("This program converts distances measured in kilometers to miles.")
    kilometers = eval(input("Enter the distance in kilometers."))
    miles = kilometers * 0.62
    print(kilometers, "kilometers is equal to", miles, "miles.")

