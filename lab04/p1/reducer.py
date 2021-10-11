#!/usr/bin/python3

import sys

result = {}
count = {}

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    word = str(key).split(',', 1)

    if word[1] == '.':
        count[word[0]] = int(value)
    else:
        result[key] = result.get(key, 0) + int(value)


for k, v in result.items():
    word = k.split(',', 1)

    print(key, v / count[word[0]])