#!/bin/

# Overview:
#   Goals of this script:
#       - Take in information from from a csv file and output break-even values
#         for a particular stock

# Outline / Plan:
#   - First glance, it might be good to make an object for each ticker that 
#     contains all the information about its purchase price, break even price,
#     how many options were used, average option price, etc. 


# Libraries
import csv
import os
import pandas as pd
import sys


# TODO: See other python script. Add this to global library
global_error = "Error: "


def analyzeCsv( pPath ):
    # Check if the file exists
    print( "Dose " + pPath + " exist?" )
    if os.path.exists( pPath ):
        print( "Yes." )
    else:
        print( "No.")
    print()
    
    # If file exists, then figure out what it does
    df = pd.read_csv( pPath, sep=',' )
    # len_row, len_col = df.shape
    # print( len_row )
    # print ( len_col )

    df.head()
    # for row in df:
    #     print( row )
    # for row in range( len_row ):
        # print( df.loc[ row ] ) # This prints in a block form, not what you want



def calc_total_commision():
    # Variables
    commision = 0

    # Cycle through every row:


def main():
    ticker_list = []
    ticker_baseprice = []
    ticker_otions = []
    ticker_breakeven = []

    # TODO: if no input, find the most recent csv
    # TODO: Could make this into a function. Things could be more complicated with the year
    
    # Selects the path to csv to analyze
    if len( sys.argv ) == 2:
        csv_input_path = sys.argv[ 1 ]
    
    elif len( sys.argv ) > 2:
        csv_input_path = global_error + "More than 2 arguments"
        return -1
        
    else:
        # TODO: This file name is the same as in convert_csv_td.py
        # relative_path =
        # csv_input_name = 'output.csv'
        csv_input_name = 'testing.csv'
        csv_input_path = 'filter_csv_file/output/' + csv_input_name
        
    analyzeCsv( csv_input_path )
    


if __name__ == "__main__":
    main()