# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Assign the relative path
csvpath = 'Module_Three_Challenge/PyPoll/Resources/election_data.csv'

# Initialize variables for total number of votes and candidates who received votes
total_votes = 0
candidates = {}

# Read the data from the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        print(row)