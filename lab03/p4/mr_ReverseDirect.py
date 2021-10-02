import re
from mrjob.job import MRJob

class Graph(MRJob):

    def mapper(self, _, value):
        nodes = value.split(" ")
        fromNode = nodes[0]

        for node in nodes[1:]:
            yield node, fromNode
    
    def reducer(self, key, values):
        yield key, " ".join(sorted(list(values)))



if __name__ == '__main__':
    Graph.run()
