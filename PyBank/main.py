# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Assign the relative path
csvpath = 'Module_Three_Challenge/PyBank/Resources/budget_data.csv'

# Create empty lists for storing the column data
dates = []
profits_losses = []

# Read the data from the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:

        # fill the empty lists
        date = row[0]
        profit_loss = int(row[1])
        dates.append(date)
        profits_losses.append(profit_loss)

# Calculate the total number of months
total_months = len(dates)

# Calculate the net total amount of profts/losses over the entire period
net_total = sum(profits_losses)

# Calculate the changes in profits/losses over the entire period using a for loop
changes = [profits_losses[i + 1] - profits_losses[i] for i in range(len(profits_losses) - 1)]

# Calculate the average of the changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index + 1]

# Calculate the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index + 1]

# Print results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
# Format the average change to round up to two decimal places
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export a text file with the results
output_path = 'Module_Three_Challenge/PyBank/Analysis/Analysis_Results.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write("Total Months: 86\n")
    file.write("Total: $22564198\n")
    file.write("Average Change: $-8311.11\n")
    file.write("Greatest Increase in Profits: Aug-16 ($1862002)\n")
    file.write("Greatest Decrease in Profits: Feb-14 ($-1825558)\n")



