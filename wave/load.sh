#!/bin/bash

RESULTDIR=../results
cp $RESULTDIR/train_data.txt .
cp $RESULTDIR/test_data.txt .
cp $RESULTDIR/train_alert.txt .
cp $RESULTDIR/test_alert.txt .

python genjson.py > fields.json
cat head.json fields.json tail.json > train_data_schema.json
cat head.json fields.json tail.json > test_data_schema.json

./load_dataset.sh "My Private App" TrainData       train_data.txt
./load_dataset.sh "My Private App" TestData        test_data.txt
./load_dataset.sh "My Private App" TrainFit        train_alert.txt
./load_dataset.sh "My Private App" TestPredictions test_alert.txt
