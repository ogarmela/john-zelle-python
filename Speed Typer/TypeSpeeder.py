#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     27/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import math
import time
import datetime
import random
def main():
    win = GraphWin("TypeSpeeder",700,700)
    win.setCoords(0,0,700,700)

#   easy = open("H:\Profile\Desktop\Grade 12 Computer Science\My Game\easywords.txt","r")
    easy = open("C:\\Users\\brads\\Desktop\\Grade 12 Code\\My Game\\easywords.txt","r")
    easywords = easy.read()
    easysplit = easywords.splitlines()
    print(easysplit)
    randomnum1 = random.randint(0,474)
    randomword1 = easysplit[randomnum1]

#    medium = open("H:\Profile\Desktop\Grade 12 Computer Science\My Game\mediumwords.txt","r")
    medium = open("C:\\Users\\brads\\Desktop\\Grade 12 Code\\My Game\\mediumwords.txt","r")
    mediumwords = medium.read()
    mediumsplit = mediumwords.splitlines()
    print(mediumsplit)
    randomnum2 = random.randint(0,5470)
    randomword2 = mediumsplit[randomnum2]

#    hard = open("H:\Profile\Desktop\Grade 12 Computer Science\My Game\hardwords.txt","r")
    hard = open("C:\\Users\\brads\\Desktop\\Grade 12 Code\\My Game\\hardwords.txt","r")
    hardwords = hard.read()
    hardsplit = hardwords.splitlines()
    print(hardsplit)
    randomnum3 = random.randint(0,2245)
    randomword3 = hardsplit[randomnum3]


    bigword = Text(Point(350,450),randomword3)
    bigword.setSize(36)
    bigword.setFace("helvetica")
    bigword.setStyle("bold")
    bigword.draw(win)
    inputword = Entry(Point(350,50),20)
    inputword.draw(win)
    word = 0
    run = 0
    t = 0

    while True:

        if run == 0:
            starttime = datetime.datetime.now()
            run = 1
        endtime = datetime.datetime.now()
        print(starttime)
        print(endtime)


        timer = Text(Point(350,600),endtime-starttime)
        if t == 0:
            timer.draw(win)
        t = 1
        timer.setText(endtime-starttime)
        if endtime > starttime + datetime.timedelta(0,5):
            print("You lose")
            win.close()
            quit()
        key = win.checkKey()
        print(key)
        if key == "Return":
            word = inputword.getText()
            print(word)
            if word == randomword3:
                print("You win!")
                win.close()
            else:
                print("You lose!")
                win.close()
            quit()


    win.getMouse()
    win.close()

main()