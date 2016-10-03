#######################################################
# Script:
#    genFeatures.py
# Usage:
#    python genFeatures.py <input_file>
# Description:
#    Generate feature data set for performance metrics
# Authors:
#    Jasmin Nakic, jnakic@salesforce.com
#    Samir Pilipovic, spilipovic@salesforce.com
#######################################################

import sys
import math
from datetime import datetime

def getOrdinalFrac(dateObj):
    # Return the proleptic Gregorian ordinal of the date + time as date fraction
    dtFrac = dateObj.toordinal() + dateObj.hour/24.0 + dateObj.minute / 1440.0
    return dtFrac
#end getOrdinalFrac

def process(data):
    # Tab delimited file where col #1 is timestamp and col #2 is the metric value
    vals = data.split('\t')
    timeStamp = vals[0]
    cnt = int(vals[1])
    dt = datetime.strptime(timeStamp,"%y-%m-%d %H:%M")
    timeStamp = "20" + timeStamp + ":00"
    dateStr = dt.strftime("%Y-%m-%d")
    ordinalFrac = getOrdinalFrac(dt)

    dayInWeek = dt.weekday()
    weekdaySin = math.sin(dayInWeek*2*math.pi/7)
    weekdayCos = math.cos(dayInWeek*2*math.pi/7)

    hourInDay = dt.hour
    hourSin = math.sin(hourInDay*2*math.pi/24)
    hourCos = math.cos(hourInDay*2*math.pi/24)

    isMonday = 1    if dayInWeek == 0 else 0
    isTuesday = 1   if dayInWeek == 1 else 0
    isWednesday = 1 if dayInWeek == 2 else 0
    isThursday = 1  if dayInWeek == 3 else 0
    isFriday = 1    if dayInWeek == 4 else 0
    isSaturday = 1  if dayInWeek == 5 else 0
    isSunday = 1    if dayInWeek == 6 else 0

    isHour0 = 1  if hourInDay == 0 else 0
    isHour1 = 1  if hourInDay == 1 else 0
    isHour2 = 1  if hourInDay == 2 else 0
    isHour3 = 1  if hourInDay == 3 else 0
    isHour4 = 1  if hourInDay == 4 else 0
    isHour5 = 1  if hourInDay == 5 else 0
    isHour6 = 1  if hourInDay == 6 else 0
    isHour7 = 1  if hourInDay == 7 else 0
    isHour8 = 1  if hourInDay == 8 else 0
    isHour9 = 1  if hourInDay == 9 else 0
    isHour10 = 1 if hourInDay == 10 else 0
    isHour11 = 1 if hourInDay == 11 else 0
    isHour12 = 1 if hourInDay == 12 else 0
    isHour13 = 1 if hourInDay == 13 else 0
    isHour14 = 1 if hourInDay == 14 else 0
    isHour15 = 1 if hourInDay == 15 else 0
    isHour16 = 1 if hourInDay == 16 else 0
    isHour17 = 1 if hourInDay == 17 else 0
    isHour18 = 1 if hourInDay == 18 else 0
    isHour19 = 1 if hourInDay == 19 else 0
    isHour20 = 1 if hourInDay == 20 else 0
    isHour21 = 1 if hourInDay == 21 else 0
    isHour22 = 1 if hourInDay == 22 else 0
    isHour23 = 1 if hourInDay == 23 else 0

    # Generate input for each hour in a a week
    hourWeek = ""
    for d in range(0,7):
        for h in range(0,24):
            if d > 0 or h > 0:
                hourWeek += "\t"
            if d == dayInWeek and h == hourInDay:
                hourWeek += "1"
            else:
                hourWeek += "0"

    # Holidays in 2016: May 16, Jul 14 and Aug 15
    isHoliday = 0
    if ((dt.month == 5 and dt.day == 16) or
        (dt.month == 7 and dt.day == 14) or
        (dt.month == 8 and dt.day == 15)):
        isHoliday = 1

    # Print the data line
    #      1   2   3   4   5   6     7     8   9     10    11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43
    print("%s\t%s\t%s\t%s\t%s\t%.8f\t%.8f\t%s\t%.8f\t%.8f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (timeStamp, dateStr, cnt, ordinalFrac, dayInWeek, weekdaySin, weekdayCos, hourInDay, hourSin, hourCos, isMonday, isTuesday, isWednesday, isThursday, isFriday, isSaturday, isSunday, isHour0, isHour1, isHour2, isHour3, isHour4, isHour5, isHour6, isHour7, isHour8, isHour9, isHour10, isHour11, isHour12, isHour13, isHour14, isHour15, isHour16, isHour17, isHour18, isHour19, isHour20, isHour21, isHour22, isHour23, isHoliday, hourWeek))
#end process

def header():
    # Header contains titles for the prediction input data columns
    hourWeekTitle = ""
    for d in range(0,7):
        for h in range(0,24):
            if d > 0 or h > 0:
                hourWeekTitle += "\t"
            hourWeekTitle += "H_" + str(d) + "_" + str(h)
    # Print the header line
    #      1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43
    print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("timeStamp", "dateStr", "cnt", "dateFrac", "dayInWeek", "weekdaySin", "weekdayCos", "hourInDay", "hourSin", "hourCos", "isMonday", "isTuesday", "isWednesday", "isThursday", "isFriday", "isSaturday", "isSunday", "isHour0", "isHour1", "isHour2", "isHour3", "isHour4", "isHour5", "isHour6", "isHour7", "isHour8", "isHour9", "isHour10", "isHour11", "isHour12", "isHour13", "isHour14", "isHour15", "isHour16", "isHour17", "isHour18", "isHour19", "isHour20", "isHour21", "isHour22", "isHour23", "isHoliday", hourWeekTitle))

# Start
inputFileName = sys.argv[1]
linecnt = 0
with open(inputFileName) as f:
    # Simply read file line by line, skip the header line
    for line in f:
        line = line.strip()
        linecnt = linecnt + 1
        header() if linecnt == 1 else process(line) 
