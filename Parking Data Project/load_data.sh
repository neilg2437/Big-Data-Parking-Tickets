#!/bin/sh
../../start.sh
# Check if the input directory exists, if not, create it and upload data.json
/usr/local/hadoop/bin/hdfs dfs -test -d /p1/input/ || {
  /usr/local/hadoop/bin/hdfs dfs -mkdir -p /p1/input/
  /usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/data.json /p1/input/
}
../../stop.sh

