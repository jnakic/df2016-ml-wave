#######################################################
# Script:
#    trainHoliday.py
# Usage:
#    python trainHoliday.py <input_file> <output_file>
# Description:
#    Build the prediction model based on training data
#    Pass 2: prediction based on holiday info
# Authors:
#    Jasmin Nakic, jnakic@salesforce.com
#    Samir Pilipovic, spilipovic@salesforce.com
#######################################################

import sys
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

debugFlag = False

hourHolidayCols  = ["isHoliday", "isHour0", "isHour1", "isHour2", "isHour3", "isHour4", "isHour5", "isHour6", "isHour7", "isHour8", "isHour9", "isHour10", "isHour11", "isHour12", "isHour13", "isHour14", "isHour15", "isHour16", "isHour17", "isHour18", "isHour19", "isHour20", "isHour21", "isHour22", "isHour23"]
hourSundayCols  = ["isSunday", "isHour0", "isHour1", "isHour2", "isHour3", "isHour4", "isHour5", "isHour6", "isHour7", "isHour8", "isHour9", "isHour10", "isHour11", "isHour12", "isHour13", "isHour14", "isHour15", "isHour16", "isHour17", "isHour18", "isHour19", "isHour20", "isHour21", "isHour22", "isHour23"]

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

def genModel(rawData,calcData,modelName):
    # Initialize array
    X = np.zeros(rawData.shape[0])
    X = np.reshape(X,(-1,1))

    # Add columns for holidays by hour
    X = addColumns(X,rawData,hourHolidayCols)

    X[:, 2] = rawData["isHoliday"]*rawData["isHour0"]
    X[:, 3] = rawData["isHoliday"]*rawData["isHour1"]
    X[:, 4] = rawData["isHoliday"]*rawData["isHour2"]
    X[:, 5] = rawData["isHoliday"]*rawData["isHour3"]
    X[:, 6] = rawData["isHoliday"]*rawData["isHour4"]
    X[:, 7] = rawData["isHoliday"]*rawData["isHour5"]
    X[:, 8] = rawData["isHoliday"]*rawData["isHour6"]
    X[:, 9] = rawData["isHoliday"]*rawData["isHour7"]
    X[:,10] = rawData["isHoliday"]*rawData["isHour8"]
    X[:,11] = rawData["isHoliday"]*rawData["isHour9"]
    X[:,12] = rawData["isHoliday"]*rawData["isHour10"]
    X[:,13] = rawData["isHoliday"]*rawData["isHour11"]
    X[:,14] = rawData["isHoliday"]*rawData["isHour12"]
    X[:,15] = rawData["isHoliday"]*rawData["isHour13"]
    X[:,16] = rawData["isHoliday"]*rawData["isHour14"]
    X[:,17] = rawData["isHoliday"]*rawData["isHour15"]
    X[:,18] = rawData["isHoliday"]*rawData["isHour16"]
    X[:,19] = rawData["isHoliday"]*rawData["isHour17"]
    X[:,20] = rawData["isHoliday"]*rawData["isHour18"]
    X[:,21] = rawData["isHoliday"]*rawData["isHour19"]
    X[:,22] = rawData["isHoliday"]*rawData["isHour20"]
    X[:,23] = rawData["isHoliday"]*rawData["isHour21"]
    X[:,24] = rawData["isHoliday"]*rawData["isHour22"]
    X[:,25] = rawData["isHoliday"]*rawData["isHour23"]

    # Add columns for holidays by hour
    X = addColumns(X,rawData,hourSundayCols)

    X[:,27] = rawData["isSunday"]*rawData["isHour0"]
    X[:,28] = rawData["isSunday"]*rawData["isHour1"]
    X[:,29] = rawData["isSunday"]*rawData["isHour2"]
    X[:,30] = rawData["isSunday"]*rawData["isHour3"]
    X[:,31] = rawData["isSunday"]*rawData["isHour4"]
    X[:,32] = rawData["isSunday"]*rawData["isHour5"]
    X[:,33] = rawData["isSunday"]*rawData["isHour6"]
    X[:,34] = rawData["isSunday"]*rawData["isHour7"]
    X[:,35] = rawData["isSunday"]*rawData["isHour8"]
    X[:,36] = rawData["isSunday"]*rawData["isHour9"]
    X[:,37] = rawData["isSunday"]*rawData["isHour10"]
    X[:,38] = rawData["isSunday"]*rawData["isHour11"]
    X[:,39] = rawData["isSunday"]*rawData["isHour12"]
    X[:,40] = rawData["isSunday"]*rawData["isHour13"]
    X[:,41] = rawData["isSunday"]*rawData["isHour14"]
    X[:,42] = rawData["isSunday"]*rawData["isHour15"]
    X[:,43] = rawData["isSunday"]*rawData["isHour16"]
    X[:,44] = rawData["isSunday"]*rawData["isHour17"]
    X[:,45] = rawData["isSunday"]*rawData["isHour18"]
    X[:,46] = rawData["isSunday"]*rawData["isHour19"]
    X[:,47] = rawData["isSunday"]*rawData["isHour20"]
    X[:,48] = rawData["isSunday"]*rawData["isHour21"]
    X[:,49] = rawData["isSunday"]*rawData["isHour22"]
    X[:,50] = rawData["isSunday"]*rawData["isHour23"]

    XnoHS = np.zeros(rawData.shape[0])
    XnoHS = (1-rawData["isHoliday"])*(1-rawData["isSunday"])*calcData["predHourWeek"]
    XnoHS = np.reshape(XnoHS,(-1,1))
    X = np.append(X,XnoHS,1)

    if debugFlag:
        print "X 0: ", X[0:5]

    Y = np.copy(rawData["cnt"])
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

def writeResult(output,rawData,calcData,p5):
    # generate result file
    result = np.array(np.empty(rawData.shape[0]), dtype=[("timeStamp","|S19"),("dateFrac",float),("isHoliday",int),("isSunday",int),("cnt",int),("predSimple",int),("predTrig",int),("predHourDay",int),("predHourWeek",int),("predHS",int)])

    result["timeStamp"]    = rawData["timeStamp"]
    result["dateFrac"]     = rawData["dateFrac"]
    result["isHoliday"]    = rawData["isHoliday"]
    result["isSunday"]     = rawData["isSunday"]
    result["cnt"]          = rawData["cnt"]
    result["predSimple"]   = calcData["predSimple"]
    result["predTrig"]     = calcData["predTrig"]
    result["predHourDay"]  = calcData["predHourDay"]
    result["predHourWeek"] = calcData["predHourWeek"]
    result["predHS"]  = p5

    if debugFlag:
        print "R 0-5: ", result[0:5]
    hdr = "timeStamp\tdateFrac\tisHoliday\tisSunday\tcnt\tpredSimple\tpredTrig\tpredHourDay\tpredHourWeek\tpredHS"
    np.savetxt(output,result,fmt="%s",delimiter="\t",header=hdr,comments="")
#end writeResult

# Start
inputFileName = sys.argv[1]
hourlyFileName = sys.argv[2]
outputFileName = sys.argv[3]

# All input columns - data types are strings, float and int
trainData = np.genfromtxt(inputFileName, dtype=("|S19","|S10",int,float,int,float,float,int,float,float,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int), delimiter='\t', names=True)

# timeStamp dateFrac isHoliday isSunday cnt predSimple predTrig predHourDay predHourWeek
hourlyData = np.genfromtxt(hourlyFileName, dtype=("|S19",float,int,int,int,int,int,int,int), delimiter='\t', names=True)

PHS = genModel(trainData,hourlyData,"modelExc")
writeResult(outputFileName,trainData,hourlyData,PHS)
