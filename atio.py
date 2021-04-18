#!/usr/bin/env python3.8
import re

def atoipy(inp):
    inp = inp.strip()
    #print(inp)
    atio_regex = re.compile(r'^[+-]?\d+')
    atio_search = atio_regex.search(inp)
    if atio_search == None:
        return(0)
    else:
        int_val = int(atio_search.group())
        if int_val > (2**31)-1:
            return ((2**31)-1)
        elif int_val < -((2**31)-1):
            return (-((2**31)-1))
        else:
            return(int_val)



if __name__ == '__main__':
    inp = "    -324243foobar"
    x = atoipy(inp)
    print(x)
