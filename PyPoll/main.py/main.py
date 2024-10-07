import csv
import os
# File paths
input_file = 'election_data.csv'
output_file = 'PyPoll_Analysis.txt'

# Initialize variables
total_votes = 0
candidates = {}

file_path = os.path.join("..", "Resources", "election_data.csv")
with open(file_path) as csvfile:

# Read the CSV file

    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner based on popular vote
winner = max(candidates, key=candidates.get)

# Prepare the output string
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"
output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results
print(output)

# Write the results to a text file
with open(output_file, 'w') as text_file:
    text_file.write(output)