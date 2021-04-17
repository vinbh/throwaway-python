#!/usr/bin/env python3.8
from collections import  defaultdict

d = defaultdict(int)
with open("big-file") as fhand:
    for var in fhand:
        var = var.split()
        d[var[0]] = int(var[1])
print(d)
for w in sorted(d, key=d.get,reverse=True):
    print(w, d[w])
