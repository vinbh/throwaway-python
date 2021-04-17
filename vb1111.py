#!/usr/bin/env python3.8
import csv
from collections import defaultdict
with open("big-file") as fhand:
    data_csv = csv.DictReader(fhand)
    d = {}
    ls = []
    for var in data_csv:
        if int(var["status_code"]) >= 400 and int(var["status_code"]) <= 499:
            #print(var["Thanos"])
                print(f"dict now {d}")
                print(f"Checking for {[var['host']] }")
                if var["host"] in d:
                    print(f"{var['host']} in d")
                    d[var["host"]] =  d[var["host"]].append(var["path"])
                else:
                    print(f"{var['host']} NOT in d")
                    d[var["host"]] = [var["path"]]
    print(d)
