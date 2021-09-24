#!/usr/bin/python3

import sys


for line in sys.stdin:
    line = line.strip()

    words = line.split()
    
    for word in words:
        word = word.lower()
        if word[0].isalpha():
            print (word[0] + "\t" + "1")

