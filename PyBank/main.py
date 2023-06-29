# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# assigning the relative path
csvpath = 'Module_Three_Challenge/PyBank/Resources/budget_data.csv'

# create empty lists for storing the column data
dates = []
profits_losses = []

# read the data from the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row of data after the header
    for row in csvreader:
        # fill the empty lists
        date = row[0]
        profit_loss = int(row[1])
        dates.append(date)
        profits_losses.append(profit_loss)

total_months = len(dates)



