#!/bin/bash

#  Requires java to be in the path

CMDAPP=$1
CMDDATASET=$2
CMDINPUTFILE=$3

# operation allowed values are Overwrite/Upsert/Append/Delete
CMDOPERATION=Overwrite
CMDUSERNAME=`cat wave.username`
CMDPASSWORD=`cat wave.password`

java \
 -jar datasetutils-32.0.27.jar \
 --action load \
 --operation $CMDOPERATION \
 --u $CMDUSERNAME \
 --p $CMDPASSWORD \
 --app "$CMDAPP" \
 --dataset $CMDDATASET \
 --inputFile $CMDINPUTFILE
