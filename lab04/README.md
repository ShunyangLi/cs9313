# Lab 04

Running with hadoop streaming

```
mapred streaming \
 -D stream.map.output.field.separator=\\t \
 -D stream.num.map.output.key.fields=1 \
 -D mapreduce.map.output.key.field.separator=, \
 -D mapreduce.partition.keypartitioner.options=-k1,1 \
 -D mapreduce.partition.keycomparator.options=-k1,1,-k2,2n \
 -D mapreduce.job.reduces=2 \
 -input /user/comp9313/input/pg100.txt \
 -output o1 \
 -mapper mapper.py \
 -reducer reducer.py \
 -file mapper.py \
 -file reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
```