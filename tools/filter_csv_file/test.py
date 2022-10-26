#!/bin/

# Libraries
import csv
import pandas as pd
import os

# Main:
def main():
    nl = "\n"
    a = "Bought 2 CHPT Jan 14 2022 21.0 Call @ 0.02"
    b = [ "Bought", "2", "CHPT", "Jan", "14", "2022", "21.0", "Call", "@", "0.02"]

    # Results in x being each letter
    print( "Test 1 Results:")
    for x in a:
        print( x )
    print( nl + nl )

    # Results in x being each word
    print( "Test 2 Results:")
    for x in b:
        print( x )
    print( nl + nl )



if __name__ == "__main__":
    main()
