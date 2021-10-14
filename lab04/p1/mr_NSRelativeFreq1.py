import re
from mrjob.job import MRJob

class CoTermNSSPair(MRJob):
    """
    the number of reducer is more than 1,
    then to make sure key-value are in the same reducer
    we need to modify a little bit of mapper and reducer
    """

    def mapper_init(self):
        self.tmp = {}
        self.count = {}

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for i in range(0, len(words)):
            if len(words[i]):
                freq = {}
                for j in range(i + 1, len(words)):
                    if len(words[j]):
                        freq[words[j]] = freq.get(words[j], 0) + 1
                        self.count[words[i]] = self.count.get(words[i], 0) + 1
                
                # merge the information
                if words[i] in self.tmp:
                    for k, v in freq.items():
                        self.tmp[words[i]][k] = self.tmp[words[i]].get(k, 0) + int(v)
                else:
                    self.tmp[words[i]] = freq
                
    
    def mapper_final(self):
        for w, v in self.count.items():
            self.tmp[w]['*'] = v
            yield w, str(self.tmp[w])
    
    
    def reducer(self, key, values):
        
        count = {}
        for value in values:
            value = eval(value)
            for k, v in value.items():
                count[k] = count.get(k, 0) + v
        
        for k, v in count.items():
            if k == "*":
                continue

            yield key + ',' + k , v / count['*']


    SORT_VALUES = True

    JOBCONF = {
      'map.output.key.field.separator': ',',
      'mapred.reduce.tasks': 2,
      'mapreduce.partition.keypartitioner.options':'-k1,1',
      'mapreduce.job.output.key.comparator.class':'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
      'mapreduce.partition.keycomparator.options':'-k1,1 -k2,2n',
      'partitioner':'org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner' 
    }


if __name__ == '__main__':
    CoTermNSSPair.run()
