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
import pandas


def main():

    # Variables
    # TODO: find the newest file by default
    # TODO: make this runable from anywhere
    csv_input_name = "transactions.csv"
    csv_input_path = "input-files/" + csv_input_name
    csv_output_name = "output.csv"
    csv_output_path = "output/" + csv_output_name

    # Key Filters:
    filter_removal_expiration = "REMOVAL OF OPTION DUE TO EXPIRATION"
    filter_removal_assignment = "REMOVAL OF OPTION DUE TO ASSIGNMENT"
    filter_sold = "Sold"
    filter_bought = "Bought"

    # Columns
    col_date = "DATE"
    col_qauntity = "QUANTITY"
    col_symb = "SYMBOL"
    col_price = "PRICE"


    # Opens CSV file ( pandas )
    csv_reader = pandas.read_csv( csv_input_path, sep = ',', index_col = 0 )
    len_row, len_col = csv_reader.shape
    print( len_row )
    print( len_col )





if __name__ == "__main__":
    main()


