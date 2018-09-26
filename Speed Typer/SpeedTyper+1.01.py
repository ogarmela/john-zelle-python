#-------------------------------------------------------------------------------
# Name:        SpeedTyper
# Purpose:     Typing Game for Speed Improvement
#
# Author:      Brad Stevanus
#
# Created:     27/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     stevb6686@wrdsb.ca school license
#-------------------------------------------------------------------------------
from graphics import *
import math
import time
import datetime
import random

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

def moveHighlight(win, lengthword, highlight, paragraph, current, allword, showpar, key):
    P1x = (highlight.getP1()).getX()
    P1y = (highlight.getP1()).getY()
    P2x = (highlight.getP2()).getX()
    P2y = (highlight.getP2()).getY()
    highlight.undraw()
    newlengthword = len(paragraph[current])
    P2x = (P1x + (lengthword*11.25 + 11.25)) + newlengthword*11.25 + 6
    highlight = Rectangle(Point(P1x + lengthword*11.25 + 11.25, P1y), Point(P2x, P2y))
    highlight.setFill("red2")
    highlight.draw(win)
    allword.undraw()
    allword.draw(win)
    lengthword = newlengthword
    return highlight, P1x, P1y, P2x, P2y, lengthword

def checkWord(inputword, paragraph, current, score, counter, now_word):
    word = inputword.getText()
    word = word.strip()
    if word == paragraph[current - 1]:
        score = score + 1
        counter.setText("{0}/15".format(score))
        inputword.setText("")
        winner = True
    else:
        current = current - 1
        winner = False
    if current < 15:
        now_word.setText(paragraph[current])
    return current, score, winner

def checkLetter(lengthword, current, inputword, paragraph):
    currentword = inputword.getText()
    correctword = paragraph[current][:len(currentword)]
    if currentword == correctword:
        inputword.setTextColor("black")
    else:
        inputword.setTextColor("red2")

def calculatewpm(time_elapsed, t_characters, lengthword, current):
    t_characters = t_characters + lengthword

    print(t_characters)
    minute = time_elapsed / 60
    print(minute)
    wpm = t_characters/4 / minute
    print(wpm)
    return wpm, t_characters

def main():
    win = GraphWin("TypeSpeeder",700,700)
    win.setCoords(0,0,700,700)
    background = Rectangle(Point(100,450),Point(600,650))
    background.setFill("white")
    background.setWidth(4)
    background.draw(win)
    title = Text(Point(350,600), "SpeedTyper!")
    title.setFace("helvetica")
    title.setSize(30)
    title.setStyle("bold")
    title.draw(win)
    help = Text(Point(350,525),"Is a game where you must type out a random collection of\nwords in a certain amount of time. The boxes below indicate the\ndifficulty of the words. Your WPM (words per minute)\nis also displayed afterwards.")
    help.setFace("helvetica")
    help.setSize(13)
    help.draw(win)
    buttonEasy = Button(win,Point(150,350),100,100,"Easy")
    buttonEasy.rect.setFill("Green3")
    buttonEasy.activate()
    buttonMedium = Button(win,Point(350,350),100,100,"Medium")
    buttonMedium.rect.setFill("Yellow1")
    buttonMedium.activate()
    buttonHard = Button(win,Point(550,350),100,100,"Hard")
    buttonHard.rect.setFill("Orange1")
    buttonHard.activate()
    buttonQuit = Button(win,Point(350,150),100,100,"Quit")
    buttonQuit.rect.setFill("Red3")
    buttonQuit.activate()
    while True:
        click = win.getMouse()
        if buttonEasy.clicked(click):
            difficulty = 1
            break
        elif buttonMedium.clicked(click):
            difficulty = 2
            break
        elif buttonHard.clicked(click):
            difficulty = 3
            break
        elif buttonQuit.clicked(click):
            win.close()
            quit()
    win.close()

    win = GraphWin("TypeSpeeder",1000,600)
    win.setCoords(0,0,800,600)
    showpar = 0
    allword = Text(Point(400,350),showpar)
    allword.setSize(18)
    allword.setFace("courier")
    #allword.draw(win)
    inputword = Entry(Point(400,50),20)
    inputword.draw(win)
    score = 0
    counter = Text(Point(700, 500),"{0}/15".format(score))
    counter.draw(win)
    buttonQuit2 = Button(win,Point(725,75),75,75,"Quit")
    buttonQuit2.rect.setFill("Red3")
    buttonQuit2.activate()
    wpm = 0
    showWPM = Text(Point(75, 650),"WPM: {0}".format(wpm))
    showWPM.draw(win)

    while True:
        t_characters = 0
        showpar = ""
        if difficulty == 1:
            easy = open("easywords.txt","r")
            easywords = easy.read()
            easysplit = easywords.splitlines()
            paragraph = []
            for i in range(3):
                for i in range(5):
                    randomnum1 = random.randint(0,474)
                    randomword1 = easysplit[randomnum1]
                    paragraph.append(randomword1)
                    showpar = showpar + randomword1 + " "
                showpar = showpar + "\n"

        elif difficulty == 2:
            medium = open("mediumwords.txt","r")
            mediumwords = medium.read()
            mediumsplit = mediumwords.splitlines()
            paragraph = []
            for i in range(3):
                for i in range(5):
                    randomnum2 = random.randint(0,5470)
                    randomword2 = mediumsplit[randomnum2]
                    paragraph.append(randomword2)
                    showpar = showpar + randomword2 + " "
                showpar = showpar + "\n"

        else:
            hard = open("hardwords.txt","r")
            hardwords = hard.read()
            hardsplit = hardwords.splitlines()
            paragraph = []
            for i in range(3):
                for i in range(5):
                    randomnum3 = random.randint(0,2245)
                    randomword3 = hardsplit[randomnum3]
                    paragraph.append(randomword3)
                    if i != 4:
                        showpar = showpar + randomword3 + " "
                    else:
                        showpar = showpar + randomword3
                showpar = showpar + "\n"

        # Set score and current word back to zero
        current = 0
        score = 0
        # Draw all the things that need to be redrawn after each paragraph

        allword.setText(showpar)
        lengthword = len(paragraph[0])
        length1 = len(showpar.split("\n")[0])
        length2 = len(showpar.split("\n")[1])
        length3 = len(showpar.split("\n")[2])
        highlight = Rectangle(Point(400 - 3 - (length1/2) * 11.25, 380), Point(400 + 6 - (length1/2 - lengthword) * 11.25, 405))
        highlight.setFill("red2")
        highlight.draw(win)
        allword.draw(win)
        counter.setText("{0}/15".format(score))
        # Draw the timer again
        endtime = 0
        starttime = time.time()
        timer = Text(Point(400,550),round(endtime-starttime,1))
        timer.draw(win)
        now_word = Text(Point(400,300),paragraph[0])
        now_word.draw(win)
        word = 0
        t = 0

        while True:
            checkLetter(lengthword, current, inputword, paragraph)
            click2 = win.checkMouse()
            endtime = time.time()
            time_elapsed = endtime - starttime
            timer.setText(round(time_elapsed, 1))
            if time_elapsed > 60:
                win.close()
                if difficulty == 1:
                    easy.close
                elif difficulty == 2:
                    medium.close
                elif difficulty == 3:
                    hard.close
                quit()
            time.sleep(0.01)
            key = win.checkKey()
            if key == "space":
                current = current + 1
                current, score, winner = checkWord(inputword, paragraph, current, score, counter, now_word)
                if winner == True:
                    wpm, t_characters = calculatewpm(time_elapsed, t_characters, lengthword, current)
                    if current >= 15:  # If paragraph is done, new paragraph
                        score = checkWord(inputword, paragraph, current, score, counter, now_word)
                        stopText = Text(Point(400, 200),"READY?")
                        stopText.setSize(36)
                        stopText.draw(win)
                        time.sleep(2)
                        highlight.undraw()
                        timer.undraw()
                        allword.undraw()
                        stopText.undraw()
                        break
                    if current == 5 or current == 10:  # Move highlighted word down OR move it over
                        if current == 5:
                            lengthVar = length2
                        else:
                            lengthVar = length3
                        lengthword = len(paragraph[current])
                        highlight.undraw()
                        highlight = Rectangle(Point(400 - 3 - (lengthVar/2) * 11.25, 380 - current*5.5), Point(400 + 6 - (lengthVar/2 - lengthword) * 11.25, 405 - current*5.5))
                        highlight.setFill("red2")
                        highlight.draw(win)
                        allword.undraw()
                        allword.draw(win)
                    else:
                        highlight, P1x, P1y, P2x, P2y, lengthword = moveHighlight(win, lengthword, highlight, paragraph, current, allword, showpar, key)


            click2 = win.checkMouse()
            #if buttonQuit2.clicked(click2):
                #quit()



    win.getMouse()
    win.close()

main()