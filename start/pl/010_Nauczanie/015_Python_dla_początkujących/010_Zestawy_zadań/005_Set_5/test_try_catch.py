#!/usr/bin/env python3

FUNCTIONS = {
            "+" : lambda s : s[:-2] + [s[-2] + s[-1]] , 
            "*" : lambda s : s[:-2] + [s[-2] * s[-1]] ,
            "-" : lambda s : s[:-1] + [-s[-1]]
        }

s = []
while True:
    try:
        x = input("> ") # this may throw a KwyboardInterrupt exception
        try:
            number = float(x) # problems when eg float("cat"), may throw ValueError
            s.append(number) # skipped if previous command fails
        except ValueError as e:
            try:
                news = FUNCTIONS[x](s) # this may cause many problems
                s = news # skipped if previous command fails
            except: # catch all for different types of exceptions
                print("INVALID OPERATION")
        print(s)
    except KeyboardInterrupt as e:
        print("\nEXITING")
        break # gracefull exit
