colHeader = "timeStamp	dateStr	cnt	dateFrac	dayInWeek	weekdaySin	weekdayCos	hourInDay	hourSin	hourCos	isMonday	isTuesday	isWednesday	isThursday	isFriday	isSaturday	isSunday	isHour0	isHour1	isHour2	isHour3	isHour4	isHour5	isHour6	isHour7	isHour8	isHour9	isHour10	isHour11	isHour12	isHour13	isHour14	isHour15	isHour16	isHour17	isHour18	isHour19	isHour20	isHour21	isHour22	isHour23	isHoliday	H_0_0	H_0_1	H_0_2	H_0_3	H_0_4	H_0_5	H_0_6	H_0_7	H_0_8	H_0_9	H_0_10	H_0_11	H_0_12	H_0_13	H_0_14	H_0_15	H_0_16	H_0_17	H_0_18	H_0_19	H_0_20	H_0_21	H_0_22	H_0_23	H_1_0	H_1_1	H_1_2	H_1_3	H_1_4	H_1_5	H_1_6	H_1_7	H_1_8	H_1_9	H_1_10	H_1_11	H_1_12	H_1_13	H_1_14	H_1_15	H_1_16	H_1_17	H_1_18	H_1_19	H_1_20	H_1_21	H_1_22	H_1_23	H_2_0	H_2_1	H_2_2	H_2_3	H_2_4	H_2_5	H_2_6	H_2_7	H_2_8	H_2_9	H_2_10	H_2_11	H_2_12	H_2_13	H_2_14	H_2_15	H_2_16	H_2_17	H_2_18	H_2_19	H_2_20	H_2_21	H_2_22	H_2_23	H_3_0	H_3_1	H_3_2	H_3_3	H_3_4	H_3_5	H_3_6	H_3_7	H_3_8	H_3_9	H_3_10	H_3_11	H_3_12	H_3_13	H_3_14	H_3_15	H_3_16	H_3_17	H_3_18	H_3_19	H_3_20	H_3_21	H_3_22	H_3_23	H_4_0	H_4_1	H_4_2	H_4_3	H_4_4	H_4_5	H_4_6	H_4_7	H_4_8	H_4_9	H_4_10	H_4_11	H_4_12	H_4_13	H_4_14	H_4_15	H_4_16	H_4_17	H_4_18	H_4_19	H_4_20	H_4_21	H_4_22	H_4_23	H_5_0	H_5_1	H_5_2	H_5_3	H_5_4	H_5_5	H_5_6	H_5_7	H_5_8	H_5_9	H_5_10	H_5_11	H_5_12	H_5_13	H_5_14	H_5_15	H_5_16	H_5_17	H_5_18	H_5_19	H_5_20	H_5_21	H_5_22	H_5_23	H_6_0	H_6_1	H_6_2	H_6_3	H_6_4	H_6_5	H_6_6	H_6_7	H_6_8	H_6_9	H_6_10	H_6_11	H_6_12	H_6_13	H_6_14	H_6_15	H_6_16	H_6_17	H_6_18	H_6_19	H_6_20	H_6_21	H_6_22	H_6_23"

colList = colHeader.split("\t")

# debug print colList

for idx in range(0,len(colList)):

    # debug print idx, ":", colList[idx]

    # Common column attributes
    if idx == 0:
        print '    "fields" : [ {'
    else:
        print '    }, {'
    print '      "name" : "'+colList[idx]+'",'
    print '      "fullyQualifiedName" : "'+colList[idx]+'",'
    print '      "label" : "'+colList[idx]+'",'
    print '      "description" : "'+colList[idx]+'",'

    if colList[idx] == "timeStamp":
        print '      "type" : "Text",'
        print '      "defaultValue" : null,'
        print '      "precision" : 20,'
        print '      "isMultiValue" : false,'

    elif colList[idx] == "dateStr":
        print '      "type" : "Date",'
        print '      "defaultValue" : null,'
        print '      "format" : "yyyy-MM-dd",'
        print '      "fiscalMonthOffset" : 0,'
        print '      "firstDayOfWeek" : 1,'
        print '      "isYearEndFiscalYear" : true,'

    elif colList[idx] == "dateFrac" or colList[idx] == "weekdaySin" or colList[idx] == "weekdayCos" or colList[idx] == "hourSin" or colList[idx] == "hourCos":
        print '      "type" : "Numeric",'
        print '      "precision" : 12,'
        print '      "scale" : 5,'
        print '      "defaultValue" : "0",'
        print '      "format" : null,'

    else:
        print '      "type" : "Numeric",'
        print '      "precision" : 10,'
        print '      "scale" : 0,'
        print '      "defaultValue" : "0",'
        print '      "format" : null,'

    # Common column attributes
    print '      "canTruncateValue" : true,'
    print '      "isSkipped" : false'
