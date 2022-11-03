#!/bin/

# Libraries
import csv
import pandas as pd
import os
import sys

# Main:
def main():
    if len(sys.argv) == 2:
        name = sys.argv[1]
    elif len(sys.argv) > 2:
        name = "more than 2 argument:"
        for i in sys.argv:
            print(i)
    else:
        name = "< no argument >"
    
    print(name)
    # nl = "\n"
    # a = "Bought 2 CHPT Jan 14 2022 21.0 Call @ 0.02"
    # b = [ "Bought", "2", "CHPT", "Jan", "14", "2022", "21.0", "Call", "@", "0.02"]

    # # Results in x being each letter
    # print( "Test 1 Results:")
    # for x in a:
    #     print( x )
    # print( nl + nl )

    # # Results in x being each word
    # print( "Test 2 Results:")
    # for x in b:
    #     print( x )
    # print( nl + nl )



if __name__ == "__main__":
    main()
