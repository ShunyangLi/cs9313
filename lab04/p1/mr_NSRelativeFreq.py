import re
from mrjob.job import MRJob

class CoTermNSSPair(MRJob):
    """
    the number of reducer is 1,
    then we can use map separator
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
            yield w + ',.', v
            for u, num in self.tmp[w].items():
                yield w + ',' + u, num
    

    def reducer_init(self):
        self.total = 0
    
    def reducer(self, key, values):
        word = str(key).split(',', 1)
        
        if word[1] == '.':
            self.total = sum(values)
        else:
            yield key, sum(values) / self.total
                

    SORT_VALUES = True

    JOBCONF = {
      'map.output.key.field.separator': ',',
      'mapred.reduce.tasks': 3,
      'mapreduce.partition.keypartitioner.options':'-k1,1',
      'partitioner':'org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner',
      'mapreduce.partition.keycomparator.options':'-k1,1 -k2,2n',
      'mapreduce.job.output.key.comparator.class':'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator'
    }



if __name__ == '__main__':
    CoTermNSSPair.run()
