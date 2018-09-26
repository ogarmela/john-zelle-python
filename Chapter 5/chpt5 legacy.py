#-------------------------------------------------------------------------------
# Name:        Chapter 5
# Purpose:
#
# Author:      stevb6686
#
# Created:     06/10/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import time
import random

# True/False

# 1. False
# 2. True
# 3. False
# 4. True
# 5. True
# 6. True
# 7. True
# 8. False
# 9. False
# 10. False

# Multiple Choice

# 1. d
# 2. c
# 3. a
# 4. c
# 5. c
# 6. d
# 7. d
# 8. c
# 9. c
# 10. a

# Discussion Questions

# 1.
# a) The Knights who say, ni!
# b) spamspamspamni!ni!
# c) p
# d) pa
# e) ani
# f) spam!
# g) SPAM
# h) NI! NI! NI!

# 2.
# a) s2[:2].upper()
# b) s2 + s1 + s2
# c) ((s1.capitalize() + " " + s2.capitalize() + " ") * 3)[:-1]
# d) s1
# e) s1[0:2],s1[-1]

# 3.
# a)
# a
# a
# r
# d
# v
# a
# r
# k
# b)
# Now
# is
# the
# winter
# of
# our
# discontent...
# c)
# M ss ss pp
# d)
# scrt
# e)
# tfdsfu

# 4.
# a) Looks like spam and eggs for breakfast
# b) There is 1 spam 4 you
# c) Hello Susan
# d) 2.30 2.30
# e) Illegal because the index is out of range (called expr 7 when only 0 and 1 exist)
# f) Time left 01:37.37
# g) Illegal because the index is out of range (called expr 1 when only 0 exists)

# 5.
# Public key encryption is more useful for securing communications on the
# Internet than private (shared) key encryption because in a private key
# encryption setup, if a user gets ahold of the encryption key, they can decrypt
# the message because both keys are the same.
# However, in a public key encryption, the encryption key can be viewed publicly,
# while the decryption key is kept private. This allows your browser or other
# communications system to send encrypted data that only the company or object
# on the other end knows how to decode.

def main2():
    inGrade = eval(input("Enter your 5-point quiz score: \n"))
    letter = ["F","F","D","C","B","A"]
    grade =  str(inGrade) + "-" + letter[inGrade]
    print("Your score is {0}.".format(grade))

def main4():
    phrase = input("Enter a phrase to get an acronym: ")
    acr = ""
    for word in phrase.split():
        acr = acr + word[0]
    acr = acr.upper()
    print("The acronym of {0} is {1}".format(phrase, acr))

def main6():
    sum = 0
    inName = input("Enter a name to be summed up")
    for word in inName.split():
        word = word.lower()
        for ch in word:
            sum = sum + (ord(ch) - 96)
    print("The total value of your name is {0}".format(sum))

def main8():
    encrypt = ""
    message = input("Enter the message to be encoded:")
    key = eval(input("Enter the key:"))
    for ch in message:
        if ch.isupper():
            ch = ord(ch) + key
            if ch > 90:
                ch = ch - 26
            ch = chr(ch)
        elif ch.islower():
            ch = ord(ch) + key
            if ch > 122:
                ch = ch - 26
            ch = chr(ch)
        else:
            ch = chr(ord(ch) + key)
        encrypt = encrypt + ch
    print("The encrypted message is:",encrypt)

def main10():
    string = input("Enter a sentence to take the average word length:")
    x = 0
    length = 0
    for word in string.split():
        length = length + len(word)
        x = x + 1
    avg = length / x
    print("The average word length in the sentence is {0}".format(avg))

def main12():
    print("This program calculates the future value")
    print("of your money after the amount of years that were invested.\n")
    principal,apr,years = eval(input("Enter the initial principal,\nannual interest rate,\nand the # of years for your investment."))
    #apr = eval(input("Enter the annual interest rate (%): "))
    #years = eval(input("Enter the number of years for your investment."))
    print("Year       Value")
    print("------------------")
    print(" {0:<8}${1:<8.2f}".format(0,principal))
    for i in range(years):
        principal = principal * (1 + apr/100)
        print(" {0:<8}${1:<8.2f}".format(i+1,principal))

def main14():
    file = input("Enter the address of the file to be calculated.")
    inFile = open(file,"r")
    lines = inFile.readlines()
    linecount = 0
    wordcount = 0
    chcount = 0
    for line in lines:
        linecount = linecount + 1
    for line in lines:
        for word in line.split():
            wordcount = wordcount + 1
    for line in lines:
        for word in line.split():
            for ch in word:
                chcount = chcount + 1
    inFile.close()
    print("This file has {0} lines.".format(linecount))
    print("This file has {0} words.".format(wordcount))
    print("This file has {0} characters.".format(chcount))

def main16():
    askFile = input("Enter the address of the file with the quiz scores.")
    inFile = open(askFile,"r")
    lines = inFile.readlines()
    scores = ""
    list = []
    for line in lines:
        line = line[:-1]
        scores = scores + line
    print(scores)
    for x in range(11):
        cc = scores.count(str(x))
        list.append(cc)
    print(list)
    win = GraphWin("Quiz Scores",600,450)
    win.setCoords(0,0,600,450)
    xline = Line(Point(50,50),Point(600,50))
    xline.setWidth(3)
    xline.draw(win)
    yline = Line(Point(50,50),Point(50,450))
    yline.setWidth(3)
    yline.draw(win)
    move = 75
    for x in range(11):
        xscore = Text(Point(move,25),"{0}".format(x))
        xscore.draw(win)
        move = move + 50
    move = 50
    for x in range(8):
        yscore = Text(Point(25,move),"{0}".format(x*2))
        yscore.draw(win)
        move = move + 50
    move = 55
    for x in range(11):
        drawscore = list[x] * 25
        bar = Rectangle(Point(move,50),Point(move+40,50+drawscore))
        bar.setFill("green2")
        bar.draw(win)
        move = move + 50
    Text(Point(300,410),"Click to close.\ny = Number of scores\nx = Quiz scores").draw(win)

    win.getMouse()
    win.close()






