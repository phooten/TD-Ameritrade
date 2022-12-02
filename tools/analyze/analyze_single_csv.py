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

def StrRound( pNumber, pDec=2):
    return str( round( pNumber, pDec ) )

# TODO: Split up analyze CSV into smaller functions
def doesFileExist( pPath ):
    # Check if the file exists
    print( "Does " + pPath + " exist?" )
    if os.path.exists( pPath ):
        print( "The path " + pPath + " exists." )
    else:
        print( "No. Script stopping. It's returning.")
        return
    print()


def findUniqueTickers( pPath ):
    df = pd.read_csv( pPath, sep=',' )
    len_row, len_col = df.shape

    ticker_list = []

    for row in range( len_row - 1 ):
        curr = df.loc[ row, "TICKER" ]
        if curr not in ticker_list:
            if not any( x in str( curr ) for x in ["nan", "NOT DONE"] ):
                ticker_list.append( curr )

    ticker_list = sorted( ticker_list )
    
    print( 'Unique tickers: ' + str( len( ticker_list ) ) )

    return ticker_list

def analyzeCsv( pPath, pTicker ):
    # If file exists, then figure out what it does
    df = pd.read_csv( pPath, sep=',' )
    len_row, len_col = df.shape
        
    # TODO: User can select total of everything, or total of single items
    # Start of Logic:
    #   ** Order of want **
    #   - Break Even:
    #       - Overall options
    #   - total commission
    #   - # of stock currently own
    #   - how many options trades

    total_pl = 0            # profit / loss
    total_commission = 0
    opt_comission = 0
    opt_trades = 0
    total_stock = 0
    stock_trades = 0

    for row in range( len_row - 1 ):

        curr = df.loc[ row, "TICKER" ]
        if( curr == pTicker ):

            action = df.loc[ row, "ACTION" ]
            amount = df.loc[ row, "AMOUNT" ]
            comm = df.loc[ row, "TOTAL COMMISION" ]
            cost = df.loc[ row, "COST" ]
            group = df.loc[ row, "TYPE" ]

            if NaN != str( comm ) :
                    total_commission += float( comm )

            if any( tmp in group for tmp in [ "Put", "Call" ] ):
                opt_trades += 1
                
                # TODO: Spell correct commission
                # Counts total commisions
                if NaN != str( comm ) :
                    opt_comission += float( comm )

            if NaN != str( cost ):
                if action == "Bought":
                    total_pl -= cost

                elif action == "Sold":
                    total_pl += cost

                else:
                    print( "ISSUE: COST" )

            # TODO: Need to finish the Assignment portion of the xml
            if group == "Stock":
                if action == "Bought":
                    total_stock -= amount

                elif action == "Sold":
                    total_stock += amount

                else:
                    print( "ISSUE: AMOUNT" )
            #elif group == "Assigment":
                #if 
                    
                #elif

        # curr = df.loc[ row, "TICKER" ]
        # for i in range( len( mult_ticker_lst ) ):
        #     if curr == mult_ticker_lst[ i ]:
        #         mult_ticker_count[ i ] += 1
        #         if NaN != str( df.loc[ row, "TOTAL COMMISION" ] ):
        #             mult_commission_count[ i ] = float( df.loc[ row, "TOTAL COMMISION" ] )

    # Final formatting
    total_pl *= 100

    # Printing out values
    print( 'Stock:              ' + pTicker )
    print( 'Total Commision:  $ ' + StrRound( total_commission ) ) 
    print( 'Option Commision: $ ' + StrRound( opt_comission ) )
    print( 'Option Trades:      ' + str( opt_trades ) )
    print( 'Total P/L:        $ ' + StrRound( total_pl ) )
    print( 'Current Stock:      ' + str( total_stock ) )
    print( '\n')


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
        csv_input_name = 'testing.csv'
        csv_input_path = '../../io/output/' + csv_input_name


    if( False == doesFileExist( csv_input_path ) ):
        exit( 1 )


    user_input = input( 'Enter a Ticker for single, or <enter> for all...  ' )
    if user_input == '':
        ticker_list = findUniqueTickers( csv_input_path )

    else:
        ticker_list = [ user_input ]

    for ticker in ticker_list:
        # print( str( ticker ) )
        analyzeCsv( csv_input_path, ticker )




if __name__ == "__main__":
    main()
