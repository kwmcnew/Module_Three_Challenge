# Module_Three_Challenge

# For the PyBank script, I had a session with a tutor and he suggested that I set up empty lists for "dates" and "profits_losses" before running a for loop, and then use the for loop to fill the lists:
dates = []
profits_losses = []
 # Read each row of data after the header
    for row in csvreader:

        # fill the empty lists
        date = row[0]
        profit_loss = int(row[1])
        dates.append(date)
        profits_losses.append(profit_loss)

# Also for the PyBank script, I used a strategy I found on Stack Overflow for calculating the changes in profits/losses over the entire period using a for loop embedded in a list
changes = [profits_losses[i + 1] - profits_losses[i] for i in range(len(profits_losses) - 1)]

# I also referenced Stack Overflow to come up with a quick way to calculate the greatest increase and decrease in profits
  greatest_increase = max(changes)
  greatest_increase_index = changes.index(greatest_increase)
  greatest_increase_date = dates[greatest_increase_index + 1]

  greatest_decrease = min(changes)
  greatest_decrease_index = changes.index(greatest_decrease)
  greatest_decrease_date = dates[greatest_decrease_index + 1]

# For the PyPoll script, I referenced the course material, Stack Overflow, and a site called W3Schools to come up with strategies for using python dictionaries to calculate the data:
        candidates = {}
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
