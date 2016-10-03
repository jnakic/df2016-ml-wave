#######################################################
# Script:
#    trainPerf.py
# Usage:
#    python trainPerf.py <input_file> <output_file>
# Description:
#    Build the prediction model based on training data
#    Pass 1: prediction based on hours in a week
# Authors:
#    Jasmin Nakic, jnakic@salesforce.com
#    Samir Pilipovic, spilipovic@salesforce.com
#######################################################

import sys
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

debugFlag = False
# Feature lists for different models
simpleCols = ["dateFrac"]
trigCols = ["dateFrac", "weekdaySin", "weekdayCos", "hourSin", "hourCos"]
hourDayCols  = ["dateFrac", "isMonday", "isTuesday", "isWednesday", "isThursday", "isFriday", "isSaturday", "isSunday", "isHour0", "isHour1", "isHour2", "isHour3", "isHour4", "isHour5", "isHour6", "isHour7", "isHour8", "isHour9", "isHour10", "isHour11", "isHour12", "isHour13", "isHour14", "isHour15", "isHour16", "isHour17", "isHour18", "isHour19", "isHour20", "isHour21", "isHour22", "isHour23"]
hourWeekCols = ["dateFrac"]
for d in xrange(0,7):
    for h in xrange(0,24):
        hourWeekCols.append("H_" + str(d) + "_" + str(h))

def addColumns(dest, src, colNames):
    # Initialize temporary array
    tmpArr = np.empty(src.shape[0])
    cols = 0
    # Copy column content
    for name in colNames:
        if cols == 0: # first column
            tmpArr = np.copy(src[name])
            tmpArr = np.reshape(tmpArr,(-1,1))
        else:
            tmpCol = np.copy(src[name])
            tmpCol = np.reshape(tmpCol,(-1,1))
            tmpArr = np.append(tmpArr,tmpCol,1)
        cols = cols + 1
    return np.append(dest,tmpArr,1)
#end addColumns

def genModel(data,colList,modelName):
    # Initialize array
    X = np.zeros(data.shape[0])
    X = np.reshape(X,(-1,1))

    # Add columns
    X = addColumns(X,data,colList)

    if debugFlag:
        print "X 0: ", X[0:5]

    Y = np.copy(data["cnt"])
    if debugFlag:
        print "Y 0: ", Y[0:5]

    model = linear_model.LinearRegression()
    print model.fit(X, Y)

    print "INTERCEPT: ", model.intercept_
    print "COEFFICIENT shape: ", model.coef_.shape
    print "COEFFICIENT values: ", model.coef_
    print "SCORE values: ", model.score(X,Y)

    P = model.predict(X)
    if debugFlag:
        print "P 0-5: ", P[0:5]

    joblib.dump(model,modelName)
    return P
#end genModel

def writeResult(output,data,p1,p2,p3,p4):
    # generate result file
    result = np.array(np.empty(data.shape[0]), dtype=[("timeStamp","|S19"),("dateFrac",float),("isHoliday",int),("isSunday",int),("cnt",int),("predSimple",int),("predTrig",int),("predHourDay",int),("predHourWeek",int)])

    result["timeStamp"]    = data["timeStamp"]
    result["dateFrac"]     = data["dateFrac"]
    result["isHoliday"]    = data["isHoliday"]
    result["isSunday"]     = data["isSunday"]
    result["cnt"]          = data["cnt"]
    result["predSimple"]   = p1
    result["predTrig"]     = p2
    result["predHourDay"]  = p3
    result["predHourWeek"] = p4

    if debugFlag:
        print "R 0-5: ", result[0:5]
    hdr = "timeStamp\tdateFrac\tisHoliday\tisSunday\tcnt\tpredSimple\tpredTrig\tpredHourDay\tpredHourWeek"
    np.savetxt(output,result,fmt="%s",delimiter="\t",header=hdr,comments="")
#end writeResult

# Start
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
# All input columns - data types are strings, float and int
trainData = np.genfromtxt(inputFileName, dtype=("|S19","|S10",int,float,int,float,float,int,float,float,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int), delimiter='\t', names=True)

P1 = genModel(trainData,simpleCols,"modelSimple")
P2 = genModel(trainData,trigCols,"modelTrig")
P3 = genModel(trainData,hourDayCols,"modelHourDay")
P4 = genModel(trainData,hourWeekCols,"modelHourWeek")

writeResult(outputFileName,trainData,P1,P2,P3,P4)
