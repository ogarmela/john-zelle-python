#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     01/12/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import *
from math import *
from graphics import *

# True/False:

# 1. False
# 2. False
# 3. True
# 4. True
# 5. True
# 6. True
# 7. True
# 8. False
# 9. False
# 10. False

# Multiple Choice:

# 1. b
# 2. c
# 3. d
# 4. a
# 5. c
# 6. a
# 7. b
# 8. a
# 9. a
# 10. b

def main2():
    try:
        printIntro()
        probA, probB, n = getInputs()
        winsA, winsB, shutsA, shutsB = simNGames(n, probA, probB)
        printSummary(winsA, winsB, shutsA, shutsB)
    except IOError:
        print("Error: You entered an invalid input.")
    except NameError:
        print("Error: You entered a letter instead of a number.")
    except EOFError:
        print("Error: Incorrect input.")
    except SyntaxError:
        print("Error: Your entry was in the incorrect form.")
    except:
        print("Error: General Input Error; Refer to input dialogues for instructions.")


def printIntro():
    print("This program simulates a game of raquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve. A player can win by shutout if they have 7 points")
    print("when the other team has 0. You input the number of games to simulate.\n")

def getInputs():
    a = b = 0
    while True:
        a = eval(input("What is the prob. player A wins a serve? "))
        b = eval(input("What is the prob. player B wins a serve? "))
        n = eval(input("How many games to simulate? "))
        if (a>=0 and a<=1) and (b>=0 and b<= 1) and (n>=1 and n%1==0) and (a + b !=0): break
        else: print("The probabilities cannot be less than 0 or more than 1 (or both zero), and n must be a positive whole number.")
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    shutsA = shutsB = 0
    for i in range(n):
        scoreA, scoreB, shutsA, shutsB = simOneGame(probA, probB, shutsA, shutsB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, shutsA, shutsB

def simOneGame(probA,probB,shutsA,shutsB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    if scoreA==7 and scoreB==0:
        shutsA = shutsA + 1
    elif scoreB==7 and scoreA ==0:
        shutsB = shutsB + 1
    return scoreA, scoreB, shutsA, shutsB

def gameOver(a, b):
    return (a==15 or b==15) or (a==7 and b==0) or (b==7 and a==0)

def printSummary(winsA, winsB, shutsA, shutsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    if winsA != 0:
        print("Wins for A: {0} ({1:0.1%}). Shutouts: {2} ({3:0.1%} of wins)".format(winsA, winsA/n, shutsA, shutsA/winsA))
    else:
        print("Wins for A: 0 (0.0%). Shutouts: 0 (0.0% of wins)")
    if winsB != 0:
        print("Wins for B: {0} ({1:0.1%}). Shutouts: {2} ({3:0.1%} of wins)".format(winsB, winsB/n, shutsB, shutsB/winsB))
    else:
        print("Wins for B: 0 (0.0%). Shutouts: 0 (0.0% of wins)")

#-------------------------------------------------------------------------------

def main4():
    try:
        printIntro1()
        probA, probB, n = getInputs1()
        winsA, winsB, longGame = simNGames1(n, probA, probB)
        printSummary1(winsA, winsB, longGame)
    except IOError:
        print("Error: You entered an invalid input.")
    except NameError:
        print("Error: You entered a letter instead of a number.")
    except EOFError:
        print("Error: Incorrect input.")
    except SyntaxError:
        print("Error: Your entry was in the incorrect form.")
    except:
        print("Error: General Input Error; Refer to input dialogues for instructions.")

def printIntro1():
    print("This program simulates a game of volleyball (using rally scoring) between two")
    print('teams called "A" and "B". The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point on the serve. Probablities must add")
    print("up to 1. Games are scored to 25 points, where a team must")
    print("lead by 2 points. Reaching 1000 points is an instant win.")
    print("You input the number of games to simulate.\n")

def getInputs1():
    a = b = 0
    while True:
        a = eval(input("What is the prob. player A wins a serve? "))
        b = eval(input("What is the prob. player B wins a serve? "))
        n = eval(input("How many games to simulate? "))
        if (a>=0 and a<=1) and (b>=0 and b<= 1) and (n>=1 and n%1==0) and (a + b !=0): break
        else: print("The probabilities cannot be less than 0 or more than 1, and n must be a positive whole number.")
    return a, b, n

def simNGames1(n, probA, probB):
    winsA = winsB = 0
    longGame = 0
    for i in range(n):
        scoreA, scoreB, longGame = simOneGame1(probA, probB, longGame)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, longGame

def simOneGame1(probA,probB,longGame):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver1(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                scoreA = scoreA + 1
    if scoreA > 1000 or scoreB > 1000:
        longGame = longGame + 1
    return scoreA, scoreB, longGame

def gameOver1(a, b):
    return ((a>=25 or b>=25) and (abs(a - b) >= 2)) or (a>1000 or b>1000)

def printSummary1(winsA, winsB, longGame):
    n = winsA + winsB
    print("\nGames simulated: {0}".format(n))
    if winsA != 0:
        print("Wins for A: {0} ({1:0.1%}).".format(winsA, winsA/n))
    else:
        print("Wins for A: 0 (0.0%).")
    if winsB != 0:
        print("Wins for B: {0} ({1:0.1%}).".format(winsB, winsB/n))
    else:
        print("Wins for B: 0 (0.0%).")
    print("Number of long games (over 1000 points): {0} ({1:0.1%} of games)".format(longGame,longGame/n))

#-------------------------------------------------------------------------------

def main6():
    try:
        printIntro2()
        probA, probB, n = getInputs2()
        winsA, winsB, longGame = simNGames2(n, probA, probB)
        printSummary2(winsA, winsB, longGame)
    except IOError:
        print("Error: You entered an invalid input.")
    except NameError:
        print("Error: You entered a letter instead of a number.")
    except EOFError:
        print("Error: Incorrect input.")
    except SyntaxError:
        print("Error: Your entry was in the incorrect form.")
    except:
        print("Error: General Input Error; Refer to input dialogues for instructions.")

def printIntro2():
    print("This program simulates a singles game of badminton between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point on the serve.")
    print("At 20 all, the side which gains a 2 point lead first, wins.")
    print("At 29 all, the side scoring the 30th point, wins.")
    print("You input the number of games to simulate.\n")

def getInputs2():
    a = b = 0
    while True:
        a = eval(input("What is the prob. player A wins a serve? "))
        b = eval(input("What is the prob. player B wins a serve? "))
        n = eval(input("How many games to simulate? "))
        if (a>=0 and a<=1) and (b>=0 and b<= 1) and (n>=1 and n%1==0) and (a + b !=0): break
        else: print("The probabilities cannot be less than 0 or more than 1, and n must be a positive whole number.")
    return a, b, n

def simNGames2(n, probA, probB):
    winsA = winsB = 0
    longGame = 0
    for i in range(n):
        scoreA, scoreB, longGame = simOneGame2(probA, probB, longGame)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, longGame

def simOneGame2(probA,probB,longGame):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver2(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                scoreA = scoreA + 1
    if scoreA > 1000 or scoreB > 1000:
        longGame = longGame + 1
    return scoreA, scoreB, longGame

def gameOver2(a, b):
    return ((a>20 or b>20) and abs(a - b) >= 2) or (a>29 or b>29)

def printSummary2(winsA, winsB, longGame):
    n = winsA + winsB
    print("\nGames simulated: {0}".format(n))
    if winsA != 0:
        print("Wins for A: {0} ({1:0.1%}).".format(winsA, winsA/n))
    else:
        print("Wins for A: 0 (0.0%).")
    if winsB != 0:
        print("Wins for B: {0} ({1:0.1%}).".format(winsB, winsB/n))
    else:
        print("Wins for B: 0 (0.0%).")
    print("Number of 30 point games: {0}".format(longGame))

#-------------------------------------------------------------------------------

def main8():
    try:
        printIntro3()
        n = getTheInputs()
        prob, bust = calcProb(n)
        printans(prob,n,bust)
    except:
        print("Error: You have to enter the number of games to simulate (>0).")

def printIntro3():
    print("This program simulates a game of Blackjack.")
    print("Based on multiple games, this program calculates")
    print("The probability that the dealer will bust.\n")

def getTheInputs():
    n = 0
    while n <1:
        n = eval(input("Enter the number of games to simulate:"))
    return n

def calcProb(n):
    print(n)
    bust = 0
    for i in range(n):
        bust = calcOneGame(bust)
    prob = bust/n
    return prob, bust

def calcOneGame(bust):
    total = 0
    deck = ["ace",2,3,4,5,6,7,8,9,10,10,10,10]
    while total < 17:
        pick = deck[randint(0,12)]
        if pick == "ace":
            total = hasAce(total)
        else:
            total = total + pick
    if total > 21:
        bust = bust + 1
    return bust

def hasAce(t):
    if (t + 11) <= 21 and (t + 11) >= 17:
        t = t + 11
    else:
        t = t + 1
    return t

def printans(prob,n,bust):
    print("Probability of dealer bust:\n")
    print("Games simulated: {0}".format(n))
    print("Number of dealer busts: {0}".format(bust))
    print("Probability of dealer bust: {0:0.1%}".format(prob))

#-------------------------------------------------------------------------------

def main10():
    try:
        printHelp()
        n = getValues()
        pi,h = calcPi(n)
        printOutput(n,h,pi)
    except:
        print("Error: You have to enter the number of darts to simulate (>0).")

def printHelp():
    print("This program uses Monte Carlo techniques to estimate the")
    print("value of pi. In this scenario, pi is estimated by the average")
    print("number of darts you would hit on a dart board if the circular target")
    print("was enclosed in a square cabinet.\n")

def getValues():
    n = 0
    while n <1:
        n = eval(input("Enter the number of dart throws to simulate"))
    return n

def calcPi(n):
    h = 0
    for i in range(n):
        x,y = getCoord()
        if (x**2 + y**2) <= 1:
            h = h + 1
    pi = 4*(h/n)
    return pi,h

def getCoord():
    x = 2*random()-1
    y = 2*random()-1
    return x,y

def printOutput(n,h,pi):
    print("\nNumber of darts thrown: {0}".format(n))
    print("Number of darts hit: {0}".format(h))
    print("Estimation of pi: {0}".format(pi))

#-------------------------------------------------------------------------------

def main12():
    try:
        printEntry()
        n = getStep()
        d = getDist(n)
        printConclusion(n,d)
    except:
        print("Error: You have to enter the number of games to simulate (>0).")

def printEntry():
    print("This program simulates the 'random walk', a model that represents")
    print("where you might end up if you flip a coin to decide which 2-d")
    print("direction in which you move. You input the number of steps taken.")
    print("Negative position = backwards, positive position = forwards.\n")

def getStep():
    n = 0
    while n <1:
        n = eval(input("Enter the number of steps that you take."))
    return n

def getDist(n):
    dist = 0
    for i in range(n):
        if getrandbits(1):
            dist = dist + 1
        else:
            dist = dist - 1
    return dist

def printConclusion(n,d):
    print("\nSteps taken: {0}".format(n))
    print("Final position: {0}".format(d))

#-------------------------------------------------------------------------------

def main14():
    try:
        printStarter()
        n = takeInput()
        win = draw_Window()
        d = calcStep(n,win)
    except:
        print("Error: You have to enter the number of games to simulate (>0).")

def printStarter():
    print("This program simulates the 'random walk', a model that represents")
    print("where you might end up if you flip a coin to decide which 2-d")
    print("direction in which you move. You input the number of steps taken.")
    print("Negative position = backwards, positive position = forwards.\n")

def takeInput():
    n = 0
    while n<1:
        n = eval(input("Enter the number of steps that you take."))
    return n

def draw_Window():
    win = GraphWin("Random Walk Tracer",500,500)
    win.setCoords(-50,-50,50,50)
    for i in range(10):
        Line(Point(-40 + i*10,-50), Point(-40 + i*10,50)).draw(win)
    for i in range(10):
        Line(Point(-50,-40 + i*10), Point(50, -40 + i*10)).draw(win)
    return win

def drawPath(win,x,y,a,b):
    trace = Line(Point(x,y), Point(a,b))
    trace.draw(win)

def calcStep(n,win):
    x = y = 0
    for i in range(n):
        lastx, lasty = x, y
        angle = random() * 2 * pi * 100
        x = x + cos(angle)
        y = y + sin(angle)
        drawPath(win,x,y,lastx,lasty)
    win.getMouse()
    win.close()






