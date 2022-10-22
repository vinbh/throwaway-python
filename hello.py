#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
####################################################
## Given a file, find the occourence of a words
## in a list. did this using RE
####################################################
import re


list = ["write", "line"]
#email_re = re.compile(r"([a-zA-Z\d\.-]+)@([a-z\d-]+)\.([a-zA-Z]{2,8})(/.[a-z]{2,8})?")
list_re = re.compile(r"write | line")
good_count = 0
with open("regions") as fhand:
    for var in fhand.readlines():
        var = var.strip()
        if re.search(list_re, var):

        #if a != None:
        #var = var.strip()
            good_count += 1
            #print(a.group())
            print(re.search(list_re, var))    
    print(f"{good_count} : these are good word count")
