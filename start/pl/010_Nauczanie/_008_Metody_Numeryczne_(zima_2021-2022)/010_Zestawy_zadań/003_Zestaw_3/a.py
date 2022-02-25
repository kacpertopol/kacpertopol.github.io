#!/usr/bin/env python

import argparse

def findBinaryExpansion(x , m):
    if(x >= 1 or x < 0 or m < 0):
        return None
    else:
        result = []
        v = 0.5
        cx = x
        cX = x
        for _ in range(m):
            digit = None
            if(cX < v):
                digit = 0
            else:
                digit = 1
            cX -= digit * v
            v *= 0.5
            result.append(digit)
        return result

if(__name__ == "__main__"):
    ## 1/10 = Subscript[0.00011001100110011001101, 2] 
    ## 1/3 = Subscript[0.010101010101010101011, 2] 
    parser = argparse.ArgumentParser(description = "Return binary expansion of number >=0 <1.")
    parser.add_argument("number" , help = "Decimal number for expansion into binary >=0 <1.")
    parser.add_argument("digits" , help = "Number of digits for binary expansion.")
    args = parser.parse_args()

    x = float(args.number)
    m = int(args.digits)

    print("(0." + "".join(list(map(str , findBinaryExpansion(x , m)))) + ")_2")
