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
from enum import Enum
import os
import pandas as pd
import sys


# TODO: See other python script. Add this to global library
global_error = "Error: "
NaN = "nan"

# TODO: Split up analyze CSV into smaller functions
    

def analyzeCsv( pPath ):
    # Check if the file exists
    print( "Does " + pPath + " exist?" )
    if os.path.exists( pPath ):
        print( "The path " + pPath + " exists." )
    else:
        print( "No. Script stopping. It's returning.")
        return
    print()
    

    # If file exists, then figure out what it does
    df = pd.read_csv( pPath, sep=',' )
    len_row, len_col = df.shape
        
    # TODO: User can select total of everything, or total of single items
    # Start of Logic:
    #   - commission count
    #   - Ticker Count
    class Mode(Enum):
        TOTAL = 1
        MULTIPLE = 2
    mode = Mode.MULTIPLE
    # mode = Mode.TOTAL

    commission = 0
    mult_ticker_lst = [ "MVIS", "PTON"]
    mult_ticker_count = []
    mult_commission_count = []
    for i in mult_ticker_lst:
        mult_ticker_count.append( 0 )
        mult_commission_count.append( 0 )

    for row in range( len_row ):
        if row != len_row - 1:

            if mode == Mode.TOTAL:
                # Commission Count
                # TODO: Spell correct commission
                curr = df.loc[ row, "TOTAL COMMISION" ]
                if NaN != str( curr ) :
                    commission += float( curr )

            elif mode == Mode.MULTIPLE:
                curr = df.loc[ row, "TICKER" ]
                for i in range( len( mult_ticker_lst ) ):
                    if curr == mult_ticker_lst[ i ]:
                        mult_ticker_count[ i ] += 1
                        if NaN != str( df.loc[ row, "TOTAL COMMISION" ] ):
                            mult_commission_count[ i ] = float( df.loc[ row, "TOTAL COMMISION" ] )

            
            
    # Prints out results
    if mode == Mode.TOTAL:
        comm_str = f'{commission:.2f}'
        print( "Total Commission:  $ " + comm_str )
        # print( "All Action Count:  $ " + comm_str )
    
    elif mode == Mode.MULTIPLE:
        print( "Ticker count: " )
        for i in range( len( mult_ticker_lst ) ):
            print( "\tTraded " + mult_ticker_lst[ i ] + " " + str( mult_ticker_count[ i ] ) + " times, spent $ " + str( f'{mult_commission_count[ i ]:.2f}') + " in commission, ")


def calc_total_commision( pDataFrame ):
    # Variables
    commision = 0
    len_row, len_col = pDataFrame.shape
    for row in range( len_row ):
        # TODO: This is hard coded, don't like
        # if pDataFrame.loc[ row, 7 ] != NaN:
        commision += int( pDataFrame.loc[ row, 7 ] )

    print( "Total Comission: " + str( commision ) )
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