import re
import sys
from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for i in range(0, len(words)):
            if len(words[i]):
                tmp = {}
                for j in range(i + 1, len(words)):
                    if len(words[j]):
                        tmp[words[j]] = tmp.get(words[j], 0) + 1
                
                yield words[i], str(tmp)
    
    def combiner(self, key, values):
        tmp_freq = {}
        for value in values:
            value = eval(value)
            for k, v in value.items():    
                tmp_freq[k] = tmp_freq.get(k, 0) + int(v)
        
        yield key, str(tmp_freq)
    
    def reducer(self, key, values):
        tmp_freq = {}
        for value in values:
            value = eval(value)
            for k, v in value.items():    
                tmp_freq[k] = tmp_freq.get(k, 0) + int(v)
        
        for kk, vv in tmp_freq.items():
            yield key, str(kk) + "    " + str(vv)

if __name__ == '__main__':
    WordCount.run()
