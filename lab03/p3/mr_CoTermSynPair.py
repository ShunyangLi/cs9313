import re
from mrjob.job import MRJob

class CoTermSynPair(MRJob):

    def mapper_init(self):
        self.tmp = {}

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for index, w in enumerate(words):
            if len(w):
                for u in words[index+1:]:
                    if len(u):
                        w_, u_ = sorted([w, u])
                        k = "{} {}".format(w_, u_)
                        self.tmp[k] = self.tmp.get(k, 0) + 1

    def mapper_final(self):
        for k, v in self.tmp.items():
            yield k, v
    
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    CoTermSynPair.run()
