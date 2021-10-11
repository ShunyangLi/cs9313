#!/usr/bin/python3

import re
import sys

# this is combiner
tmp = {}
count = {}

for line in sys.stdin:
    line = line.strip()
    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
    for i in range(0, len(words)):
        if len(words[i]):
            freq = {}
            for j in range(i + 1, len(words)):
                if len(words[j]):
                    freq[words[j]] = freq.get(words[j], 0) + 1
                    count[words[i]] = count.get(words[i], 0) + 1
            
            # merge the information
            if words[i] in tmp:
                for k, v in freq.items():
                    tmp[words[i]][k] = tmp[words[i]].get(k, 0) + int(v)
            else:
                tmp[words[i]] = freq

for w, v in count.items():
    print(w + ',.' + "\t" + str(v))
    for u, num in tmp[w].items():
        print(w + ',' + u + "\t" + str(num))