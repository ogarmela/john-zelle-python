#-------------------------------------------------------------------------------
# Name:        Babysitter.py
# Purpose:     Calculate the wage of a babysitter based on the hours inputted
#
# Author:      stevb6686
#
# Created:     14/11/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getTime(string):
    start = string.split(",")[0]
    end = string.split(",")[1]
    start = start.replace(" ","")
    end = end.replace(" ","")
    if len(start) == 6:
        start = "0" + start
    if len(end) == 6:
        end = "0" + end
    starthour = int(start[:2])
    startminute = int(start[3:5])
    endhour = int(end[:2])
    endminute = int(end[3:5])
    start = start.lower()
    end = end.lower()
    if "pm" in start:
        if starthour < 12:
            starthour = starthour + 12
    else:
        if starthour >= 12:
            starthour = starthour - 12
    if "pm" in end:
        if endhour < 12:
            endhour = endhour + 12
    else:
        if endhour >= 12:
            endhour = endhour - 12
    start_total = starthour + startminute / 60
    end_total = endhour + endminute / 60
    return start_total, end_total

def getWage(s,e):
    midnight = 24
    if (s >= 6 and s < 21) and (e >= 21 or e < 6):
        if e < s:
            RT = (21 - s) * 2.75
            OT = (e + 3) * 1.75
        else:
            RT = (21 - s) * 2.75
            OT = (e - 21) * 1.75
    elif (s >= 6 and s < 21) and (e >= 6 and e < 21):
        if e < s:
            RT = (21 - s) * 2.75
            OT = 9 * 1.75
            RT = RT + (e - 6) * 2.75
        else:
            RT = (e - s) * 2.75
            OT = 0
    elif (s >= 21 or s < 6) and (e >= 6 and e < 21):
        if e < s:
            OT = (midnight - s + 6) * 1.75
            RT = (e - 6) * 2.75
        else:
            OT = (6 - s) * 1.75
            RT = (e - 6) * 2.75
    elif (s >= 21 or s < 6) and (e >= 21 or e < 6):
        if e < s:
            if s < 6 and e < 6:
                OT = (6 - s + 3 + e) * 1.75
                RT = 15 * 2.75
            elif s >= 21 and e >= 21:
                OT = (midnight - s + 6 + e - 21) * 1.75
                RT = 15 * 2.75
            else:
                OT = (midnight - s + e) * 1.75
                RT = 0
        else:
            if (e - s) > 6:
                OT = (6 - s + e - 21) * 1.75
                RT = 15 * 2.75
            else:
                OT = (e - s) * 1.75
                RT = 0
    else:
        print("Time input error. Quitting.")
        quit()
    total = RT + OT
    total_h = OT/1.75 + RT/2.75
    return total, total_h

def main():
    try:
        print("This program takes the starting and ending times of a babysitter's shift and calculates the total bill.")
        print("The proper input method is: (hh:mm am/pm (start), hh:mm am/pm (end))\n")
        enter = input("Enter the starting and ending times, separated by a comma:")
        start_total, end_total = getTime(enter)
        total, total_h = getWage(start_total, end_total)
        print("The total hours worked is: {0:0.2f}".format(total_h))
        print("The total babysitting bill is: ${0:0.2f}".format(total))
    except KeyboardInterrupt:
        print("Program exit.")
    except:
        print("Input error; check for proper format. Program quit.")
