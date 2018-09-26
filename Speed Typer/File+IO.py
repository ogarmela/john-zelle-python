#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     19/09/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    internet = open.internet("Rockstar lyrics")
    print(internet)
    infile = open("H:\A song.txt","w")
    data = infile.write("The grapefruit method")
    infile = open("H:\A song.txt","r")
    data = infile.read()
    print(data)
main()
