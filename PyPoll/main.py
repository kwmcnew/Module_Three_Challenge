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
        
        # Pull the candidate name from the third column of the file
        candidate = row[2]

        # Increment and calculate the total vote count
        total_votes += 1

        # Fill the empty dictionary with the candidates and their vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Calculate the percentage of votes each candidate won
candidate_percentages = {}
# Syntax explanation: for "key", "value" in "dictionary".items() 
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    # Syntax explanation: dictionary[new key] = new value
    candidate_percentages[candidate] = percentage

# Identify the winner of the election based on popular vote
winner = max(candidates, key=candidates.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------") 
for candidate, votes in candidates.items(): 
    percentage = candidate_percentages[candidate]
    # Format percentage to round to three decimal places
    print(f"{candidate}: {percentage:.3f}% ({votes})")  
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export a text file with the results
output_path = 'Module_Three_Challenge/PyPoll/Analysis/Analysis_Results_PyPoll.txt'
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items(): 
        percentage = candidate_percentages[candidate]
        # Format percentage to round to three decimal places
        file.write(candidate + ": " + format(percentage, ".3f") + "% " + "(" + str(votes) + ")" + "\n")
    file.write("-------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("-------------------------\n")

