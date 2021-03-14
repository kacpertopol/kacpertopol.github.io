#!/usr/bin/env python

import argparse

def important_function(x):
    return 2 * x + 1

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description = "Module template")

    parser.add_argument("input" , help = "Input file path.")
    parser.add_argument("--test" , "-t" , action = "store_true" , help = "Run tests.")
    parser.add_argument("--fun" , "-f" , help = "Apply important_function to number.")

    args = parser.parse_args()

    input_file_contents = None
    with open(args.input , "r") as input_file:
        input_file_contents = input_file.read()

    if(args.test):
        print("Testing important_function : " , important_function(2) == 5)

    if(args.fun != None):
        print("important_function applied to " , args.fun , " : " , important_function(float(args.fun)))


