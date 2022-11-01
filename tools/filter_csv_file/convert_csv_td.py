#!/bin/

# Overview:
#   Goals of this script:
#       - convert the .csv of option trades from TD trade history to readable format
#       - show data in some sort of QT format. Maybe display the data and allow user customization?
#
#

# Outline / Plan:
#   - take in newest input file, OR argument file
#   - ensure argument exists if applicable
#   - filter through excel, and append to a new file
#   - 

# Libraries
import csv
import pandas as pd
import os


def column_filter( pRow, pColLen, pCell):
    # print( pCell )

    # Variables
    new_row = []
    
    f_call = 'Call'
    f_put = 'Put'
    f_sold = 'Sold'
    f_bought = 'Bought'
    f_assignment = 'REMOVAL OF OPTION DUE TO ASSIGNMENT'
    f_expiration = 'REMOVAL OF OPTION DUE TO EXPIRATION'
    f_margin = 'MARGIN INTEREST ADJUSTMENT'
    f_balance = 'FREE BALANCE INTEREST ADJUSTMENT'
    f_funding = 'CLIENT REQUESTED ELECTRONIC FUNDING RECEIPT'
    f_exchange = 'MANDATORY - EXCHANGE'

    
    option_col = [ f_call, f_put ]
    stock_col = [ f_sold, f_bought ]
    ticker_col = [ f_sold, f_bought ]
    row_str = pCell.split()

    # Filters out options
    if any( x in pCell for x in option_col ):
        
        # Saving values
        action = row_str[ 0 ]
        amount = row_str[ 1 ]  
        ticker = row_str[ 2 ]
        date = row_str[ 3 ] + ' ' + row_str[ 4 ] + ' ' + row_str[ 5 ]
        strike = row_str[ 6 ]
        opt_type = row_str[ 7 ]
        # row_str[ 8 ] -> None
        price = row_str[ 9 ]
        # total = 0
        
        # Creating a new row
        
        new_row.append( pRow )
        new_row.append( "DATE" )
        new_row.append( date )
        new_row.append( opt_type )
        new_row.append( action )
        new_row.append( ticker )
        new_row.append( strike )
        new_row.append( amount )
        new_row.append( price )
        # new_row.append( total )

    # Filters out Expiration
    elif f_expiration in pCell:
    # elif any( x in pCell for x in f_expiration ):
        # print("Option Expriation: " + str(pRow) + " " + pCell )
        new_row.append( pRow )
        for cur in range( pColLen - 1 ):
            new_row.append( 'NaN')

    # Filters out Assignment
    elif f_assignment in pCell:
    # elif any( x in pCell for x in f_expiration ):
        # print("Option Expriation: " + str(pRow) + " " + pCell )
        new_row.append( pRow )
        for cur in range( pColLen - 1 ):
            new_row.append( 'NaN')

    # Filters out adjustments
    elif any( x in pCell for x in ( f_balance, f_margin ) ):
        # print("Balance: " + str(pRow) + " " + pCell )
        new_row.append( pRow )
        for cur in range( pColLen - 1 ):
            new_row.append( 'NaN')

    # Filters out Assignment
    elif f_exchange in pCell:
    # elif any( x in pCell for x in f_expiration ):
        # print("Option Expriation: " + str(pRow) + " " + pCell )
        new_row.append( pRow )
        for cur in range( pColLen - 1 ):
            new_row.append( 'NaN')


    elif any( x in row_str[ 0 ] for x in stock_col ):
        new_row.append( pRow )
        for cur in range( pColLen - 1 ):
            new_row.append( 'NaN')

    # Filters out funding receipts 
    elif f_funding in pCell:
        print( "funding: " + str(pRow) )
        new_row = []
    
    else:
        print( "ERROR. Nothing found." + " " + pCell)
        new_row = []

    return new_row

        
        # s = ', '
        # ans = action + s + amount + s + ticker + s + date + s + strike + s + opt_type + s + price 
        # print( ans )
    
    # elif :


# Main:
def main():
    # Variables
    # TODO: find the newest file by default
    # TODO: make this runable from anywhere
    csv_input_name = 'transactions.csv'
    csv_input_path = 'input-files/' + csv_input_name
    csv_output_name = 'output.csv'
    csv_output_path = 'output/' + csv_output_name
    tmp_output_path = 'output/' + 'testing.csv'

    # Columns
    col_date = 'DATE'
    col_desc = 'DESCRIPTION'
    col_id = 'TRANSACTION ID'
    col_num = 'NUMBER'
    col_price = 'PRICE'
    col_qaun = 'QUANTITY'
    col_tick = 'SYMBOL'


    # Characteristics of CSV 
    df = pd.read_csv( csv_input_path, sep=',' )
    len_row, len_col = df.shape
    # print( df.columns )
    # print( df.shape )
    # print( df.dtypes )
    
    new_header = [ 'INDEX', 'DATE', 'EXPIRATION DATE', 'TYPE', 'ACTION', 'TICKER', 'STRIKE', 'AMOUNT', 'COST' ]
    new_csv = pd.DataFrame( columns=new_header )
    # new_csv.reset_index(drop=True)

    # Filters information to from descripton in every row
    df[ col_num ] = 0
    tmp_row = 0     # Used to keep track of new rows. Some of the old rows will be skipped. 
    for row in range( len_row ):
        # print( row )
        if row != len_row - 1:
            new_row = column_filter( tmp_row, len( new_header ), df.loc[ row, col_desc ] )
            # print( test )
            # print(len(test))
            if len( new_row ) == len( new_header ):
                new_csv.loc[ tmp_row ] = new_row
                tmp_row += 1

            # new_csv.append( test )
            # print( df.loc[ row, col_desc ] )
    

    # Handle the output file
    # try:
    #     os.remove( csv_output_path )
    # except:
    #     print( "No files in this path: ", csv_output_path )
    # df.to_csv( csv_output_path )
    
    # new_csv.set_index( 'INDEX' )
    try:
        os.remove( tmp_output_path )
    except:
        print( "No files in this path: ", tmp_output_path )
    new_csv.to_csv( tmp_output_path, index=False )



if __name__ == "__main__":
    main()
