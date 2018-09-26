#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     20/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import time
def main():
    win = GraphWin("getkey",200,200)
    keystring = win.checkKey()
    time.sleep(5)
    print(keystring)
    win.close()
main()