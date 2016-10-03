#!/bin/bash
#######################################################
# Script:
#    all.sh
# Usage:
#    ./all.sh
# Description:
#    Generate input data sets
#    Build the predictive model using training data
#    Get the prediction on test data
#    Detect exceptions and generate alerts
# Authors:
#    Jasmin Nakic,    jnakic@salesforce.com
#    Samir Pilipovic, spilipovic@salesforce.com
#######################################################

SCRIPTDIR=scripts
INPUTDIR=data
RESULTDIR=results

python $SCRIPTDIR/genFeatures.py $INPUTDIR/train_input.txt > $RESULTDIR/train_data.txt
python $SCRIPTDIR/genFeatures.py $INPUTDIR/test_input.txt  > $RESULTDIR/test_data.txt

python $SCRIPTDIR/trainPerf.py    $RESULTDIR/train_data.txt $RESULTDIR/train_hourly.txt
python $SCRIPTDIR/trainHoliday.py $RESULTDIR/train_data.txt $RESULTDIR/train_hourly.txt $RESULTDIR/train_holiday.txt
python $SCRIPTDIR/trainExc.py     $RESULTDIR/train_data.txt $RESULTDIR/train_hourly.txt $RESULTDIR/train_exc.txt

python $SCRIPTDIR/testPerf.py    $RESULTDIR/test_data.txt $RESULTDIR/test_hourly.txt
python $SCRIPTDIR/testHoliday.py $RESULTDIR/test_data.txt $RESULTDIR/test_hourly.txt $RESULTDIR/test_holiday.txt
python $SCRIPTDIR/testExc.py     $RESULTDIR/test_data.txt $RESULTDIR/test_hourly.txt $RESULTDIR/test_exc.txt

python $SCRIPTDIR/getAlerts.py $RESULTDIR/train_exc.txt $RESULTDIR/train_alert.txt
python $SCRIPTDIR/getAlerts.py $RESULTDIR/test_exc.txt  $RESULTDIR/test_alert.txt
