import re
from mrjob.job import MRJob

class ReverseDirect(MRJob):
    """
    For combiner there are two versions,
    you can use combiner or in-mapper combiner
    """

    def mapper(self, _, value):
        nodes = value.split(" ")
        fromNode = nodes[0]

        for node in nodes[1:]:
            yield node, fromNode
    
    def reducer(self, key, values):
        yield key, " ".join(sorted(list(values)))


    SORT_VALUES = True

    JOBCONF = {
      'map.output.key.field.separator': ',',
      'mapred.reduce.tasks': 1,
      'mapreduce.partition.keypartitioner.options':'-k1,1',
      'mapreduce.job.output.key.comparator.class':'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
      'mapreduce.partition.keycomparator.options':'-k1,1 -k2,2n'
    }


if __name__ == '__main__':
    ReverseDirect.run()