import csv
import os
# Initialize variables
total_months = 0
net_total_profit_losses = 0
previous_profit_losses = None
changes = []
dates = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]
# Open and read the CSV file
file_path = os.path.join("..", "Resources", "budget_data.csv")
with open(file_path) as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    # Process each row in the CSV
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])
        # Track total months and net total
        total_months += 1
        net_total_profit_losses += profit_losses
        dates.append(date)
        # Calculate the change if not the first month
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            # Check for greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        # Update previous month's profit/losses
        previous_profit_losses = profit_losses
# Calculate average change
average_change = sum(changes) / len(changes)
# Define the file path to save the results
output_file_path = 'financial_analysis.txt'
# Open a file in write mode to save the output
with open(output_file_path, mode='w') as output_file:
    # Print financial analysis summary
    output_file.write("Financial Analysis")
    output_file.write("----------------------------")
    output_file.write(f"Total Months: {total_months}")
    output_file.write(f"Total: ${net_total_profit_losses}")
    output_file.write(f"Average Change: ${average_change:.2f}")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
     # Print financial analysis summary
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
# Notify user that the file has been written
print(f"Financial analysis results successfully saved to {output_file_path}")
