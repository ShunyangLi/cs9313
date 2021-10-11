# Lab 04

Running with hadoop streaming

```shell
mapred streaming \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.map.output.field.separator=. \
 -D stream.num.map.output.key.fields=2 \
 -D mapreduce.map.output.key.field.separator=. \
 -D mapreduce.partition.keycomparator.options=-k2,2nr \
 -D mapreduce.job.reduces=1 \
 -input /user/comp9313/input/pg100.txt \
 -output output \
 -mapper mapper.py \
 -reducer reducer.py \
 -file mapper.py \
 -file reducer.py
```