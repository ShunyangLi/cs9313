#!/usr/bin/python3

import sys

result = {}
count = {}

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = eval(value)

    for k, v in value.items():
        count[k] = count.get(k, 0) + int(v)

    if key in result:
        for k, v in result[key].items():
            count[k] = count.get(k, 0) + v
        result[key] = count
    else:
        result[key] = count


for k, v in result.items():
    for kk, vv in v.items():
        if kk == "*":
            continue

        print(k + "," + kk, vv / v['*'])