#!/usr/bin/env python

import argparse
import numpy as np

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description = "Return ||A||_n norm for matrix A.")
    parser.add_argument("matrix" , help = "Matrix entered following the format: 1 2 3 , 4 5 6 , 7 8 9")
    parser.add_argument("norm" , help = "Norm number, 1 is the traffic norm, 2 is the Eucledean norm, ...")
    args = parser.parse_args()
    
    a = np.array(list(map(lambda r : list(map(float , r.split())) , args.matrix.split(','))))
    n = int(args.norm)

    print(np.linalg.norm(a , n))
