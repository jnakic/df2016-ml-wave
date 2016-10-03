#######################################################
# Script:
#    getAlerts.py
# Usage:
#    python getAlerts.py <input_file>
# Description:
#    Generate alerts on test predictions
# Authors:
#    Jasmin Nakic, jnakic@salesforce.com
#    Samir Pilipovic, spilipovic@salesforce.com
#######################################################

import sys
import numpy as np

debugFlag = False
DELTAHIGH = 200000
DELTALOW = -200000
PCTHIGH = 20.0
PCTLOW = -20.0

def applyRule(V,P):
    delta = (P[0] - V[0]) + (P[1] - V[1]) + (P[2] - V[2])
    sum = V[0] + V[1] + V[2]
    pct = 100.0*delta/float(sum) if sum != 0 else 100.0
    alert = ""
    if delta > DELTAHIGH and pct > PCTHIGH:
        alert = "HIGH"
    if delta < DELTALOW and pct < PCTLOW:
        alert = "LOW"
    return (alert,delta,pct)

#end applyRule

def getAlerts(data):
    X = np.zeros(data.shape[0])
    # X = np.reshape(X,(-1,1))
    v = [0,0,0]
    p = [0,0,0]
    idx = 0
    row = 0
    raiseAlert = False
    for m in np.nditer(data):
        idx = idx + 1
        v[0] = v[1] if idx > 2 else 0
        v[1] = v[2] if idx > 1 else 0
        v[2] = m['cnt']
        p[0] = p[1] if idx > 2 else 0
        p[1] = p[2] if idx > 1 else 0
        p[2] = m['predHS']
        alert = ""
        val = 0
        pct = 0
        if idx >= 3: # has enough data
            raiseAlert = True
        if raiseAlert:
            (alert,val,pct) = applyRule(v,p)
        if alert != "":
            X[row] = val
            print alert, m['timeStamp'], val, pct, "(", p[0], p[1], p[2], ") (", v[0], v[1], v[2], ")"
            idx = 0
            raiseAlert = False
        row = row + 1
    return X
#end getAlerts

def writeResult(output,calcData,A):
    # generate result file
    result = np.array(np.empty(calcData.shape[0]), dtype=[("timeStamp","|S19"),("dateFrac",float),("isHoliday",int),("isSunday",int),("cnt",int),("predSimple",int),("predTrig",int),("predHourDay",int),("predHourWeek",int),("predHS",int),("alertVal",int)])

    result["timeStamp"]    = calcData["timeStamp"]
    result["dateFrac"]     = calcData["dateFrac"]
    result["isHoliday"]    = calcData["isHoliday"]
    result["isSunday"]     = calcData["isSunday"]
    result["cnt"]          = calcData["cnt"]
    result["predSimple"]   = calcData["predSimple"]
    result["predTrig"]     = calcData["predTrig"]
    result["predHourDay"]  = calcData["predHourDay"]
    result["predHourWeek"] = calcData["predHourWeek"]
    result["predHS"]       = calcData["predHS"]
    result["alertVal"]     = A

    if debugFlag:
        print "R 0-5: ", result[0:5]
    hdr = "timeStamp\tdateFrac\tisHoliday\tisSunday\tcnt\tpredSimple\tpredTrig\tpredHourDay\tpredHourWeek\tpredHS\talertVal"
    np.savetxt(output,result,fmt="%s",delimiter="\t",header=hdr,comments="")
#end writeResult

# Start
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
# timeStamp dateFrac isHoliday isSunday cnt predSimple predTrig predHourDay predHourWeek predHS
testData = np.genfromtxt(inputFileName, dtype=("|S19",float,int,int,int,int,int,int,int,int), delimiter='\t', names=True)

AV = getAlerts(testData)
writeResult(outputFileName,testData,AV)
