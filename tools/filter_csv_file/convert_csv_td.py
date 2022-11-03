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

# Concerns Important note:
#   - This script is written with the assumption that only single legs are being
#     performed. It's already getting complicated / tedious dealing with just this. 
#     Not sure what it would look like trying to connect which options were performed
#     together. Maybe utilizing the same date would be benefitial? but what if I 
#     made two or more scalps on the same day with the same tickers? 

# Libraries
import csv
import os
import pandas as pd
import sys

# TODO: Make a library for personal use
# Global
glob_error = "ERROR: "

# Converts 'MM DD YYYY' ( month day year ) to 'MM/DD/YYYY' 
def dateFormatConversion( pDate ):
    # Variables
    date_list = pDate.split()
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    
    # TODO: switch statement isn't supported in python?
    # Assign number for month
    if month == 'Jan':
        date = '1'
    elif month == 'Feb':
        date = '2'
    elif month == 'Mar':
        date = '3'
    elif month == 'Apr':
        date = '4'
    elif month == 'May':
        date = '5'
    elif month == 'Jun':
        date = '6'
    elif month == 'Jul':
        date = '7'
    elif month == 'Aug':
        date = '8'
    elif month == 'Sep':
        date = '9'
    elif month == 'Oct':
        date = '10'
    elif month == 'Nov':
        date = '11'
    elif month == 'Dec':
        date = '12'
    else:
        print( glob_error + "date_list[0] not expected: " + month)
    
    # Finalize date format
    date += '/' + day + '/' + year

    return date

def filterDescriptionColumn( pCurrRow, pColLen, pCell, pRow ):
    # Variables: General
    f_row = []
    row_str = pCell.split()

    # Variable: Filters 
    f_assignment = 'REMOVAL OF OPTION DUE TO ASSIGNMENT'
    f_expiration = 'REMOVAL OF OPTION DUE TO EXPIRATION'
    f_exchange = 'MANDATORY - EXCHANGE'
    f_balance = 'FREE BALANCE INTEREST ADJUSTMENT'
    f_funding = 'CLIENT REQUESTED ELECTRONIC FUNDING RECEIPT'
    f_margin = 'MARGIN INTEREST ADJUSTMENT'
    f_bought = 'Bought'
    f_sold = 'Sold'
    f_call = 'Call'
    f_put = 'Put'
    f_list_option = [ f_call, f_put ]
    f_list_stock = [ f_sold, f_bought ]
    f_list_ticker = [ f_sold, f_bought ]

    
    # Filters out 'removal due to expiration'
    if f_expiration in pCell:
        f_row.append( pCurrRow )
        for cur in range( pColLen - 1 ):
            f_row.append( 'NaN')

    # Filters out 'removal due to assignment'
    elif f_assignment in pCell:
        f_row.append( pCurrRow )
        for cur in range( pColLen - 1 ):
            f_row.append( 'NaN')

    # Filters out 'balance adjustments'
    elif any( x in pCell for x in ( f_balance, f_margin ) ):
        f_row.append( pCurrRow )
        for cur in range( pColLen - 1 ):
            f_row.append( 'NaN')

    # Filters out 'all options'
    elif any( x in pCell for x in f_list_option ):
        # Saving values
        action = row_str[ 0 ]
        amount = row_str[ 1 ]  
        ticker = row_str[ 2 ]
        date = row_str[ 3 ] + ' ' + row_str[ 4 ] + ' ' + row_str[ 5 ]
        strike = row_str[ 6 ]
        opt_type = row_str[ 7 ]
        # row_str[ 8 ] is not important
        price = row_str[ 9 ]
        commision = pRow[ 6 ]

        # Convert date to MM/DD/YYY
        converted_date = dateFormatConversion( date )

        # Creating a new row
        f_row.append( pCurrRow )
        f_row.append( converted_date )
        f_row.append( opt_type )
        f_row.append( action )
        f_row.append( ticker )
        f_row.append( strike )
        f_row.append( amount )
        f_row.append( price )
        # f_row.append( total )

    # Filters out 'removal due to assignment'
    elif f_exchange in pCell:
        f_row.append( pCurrRow )
        for cur in range( pColLen - 1 ):
            f_row.append( 'NaN')

    # Filters out 'any stock buy/sell' 
    elif any( x in row_str[ 0 ] for x in f_list_stock ):
        f_row.append( pCurrRow )
        for cur in range( pColLen - 1 ):
            f_row.append( 'NaN')

    # Filters out funding receipts 
    elif f_funding in pCell:
        f_row = []
    
    # Error if anything else
    else:
        print( glob_error + "Nothing found." + " " + pCell)
        f_row = []

    return f_row


# Main:
def main():
    # TODO: find the newest file by default
    # TODO: make this runable from anywhere

    # Variables: CSV files
    csv_input_name = 'transactions.csv'
    csv_input_path = 'input-files/' + csv_input_name
    csv_output_name = 'output.csv'
    csv_output_path = 'output/' + csv_output_name
    tmp_output_path = 'output/' + 'testing.csv'


    # Checking first argument of python script
    if len( sys.argv ) == 2:
        if ".csv" not in sus.argv[1]:
            print( glob_error + "first argument is not .csv" )
            return -1
        else:
            csv_input_path = sys.argv[1]
    

    # Column Names
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
    
    
    new_header = [ 'INDEX', 'DATE OF ACTION', 'DATE OF EXPIRATION', 'TYPE', 'ACTION', 'TICKER', 'STRIKE', 'AMOUNT', 'COST' ]
    new_csv = pd.DataFrame( columns=new_header )


    # Filters information from the 'descripton' column in every row
    df[ col_num ] = 0
    refined_csv_row = 0     # Used to keep track of new rows. Some of the old rows will be skipped. 
    for row in range( len_row ):
        
        if row != len_row - 1:
            tmp_row = filterDescriptionColumn( refined_csv_row, len( new_header ) - 1, df.loc[ row, col_desc ], df.loc[ row ] )
            
            if len( tmp_row ) == len( new_header ) -1:
                # Adding in date of action
                tmp_row.insert( 1, df.loc[ row, col_date ] )
                
                # Insert new row in DataFrame
                print( tmp_row )
            # new_csv.loc[ refined_csv_row ] = tmp_row
            # refined_csv_row += 1


            # new_csv.append( test )
            # print( df.loc[ row, col_desc ] )
    

    # Handle the output file
    # try:
    #     os.remove( csv_output_path )
    # except:
    #     print( "No files in this path: ", csv_output_path )
    # df.to_csv( csv_output_path )
    
# new_csv.set_index( 'INDEX' )
# try:
#     os.remove( tmp_output_path )
# except:
#     print( "No files in this path: ", tmp_output_path )
# new_csv.to_csv( tmp_output_path, index=False )


if __name__ == "__main__":
    main()
