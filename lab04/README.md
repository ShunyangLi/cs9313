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

Running with hadoop streaming with mutiple reducers
```shell
mapred streaming \
 -D stream.map.output.field.separator=. \
 -D stream.num.map.output.key.fields=2 \
 -D mapreduce.map.output.key.field.separator=. \
 -D mapreduce.partition.keycomparator.options=-k2,2nr \
 -D mapreduce.job.reduces=2 \
 -input /user/comp9313/input/pg10.txt \
 -output o1 \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -file mapper1.py \
 -file reducer1.py
```