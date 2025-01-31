#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /p1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/data.json /p1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/p1/mapper.py -mapper ../../mapreduce-test-python/p1/mapper.py \
-file ../../mapreduce-test-python/p1/reducer.py -reducer ../../mapreduce-test-python/p1/reducer.py \
-input /p1/input/* -output /p1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/output/
../../stop.sh
