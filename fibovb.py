#!/usr/bin/python3.8
import time
from functools import lru_cache

start_time = time.time()
@lru_cache(maxsize = 1000)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibo(n-1) + fibo(n-2)

for var in range(5000):
    a = fibo(var)
    print(a)

print("time taken: %s seconds" %(time.time() - start_time))            