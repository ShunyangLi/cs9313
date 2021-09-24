import re
from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        tmp = {}
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        for word in words:
            if len(word):
                tmp[word] = tmp.get(word, 0) + 1
        
        for k, v in tmp.items():
            yield (k, v)
    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    WordCount.run()
