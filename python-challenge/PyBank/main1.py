import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("../Resources/budget_data.csv")
# Define the output text file name
output_file = "financial_analysis.txt"

# Print the header for the analysis
print("Financial Analysis")
print("___________________")

# Function to calculate the average change between numbers
def calculate_average_change(numbers):
    total_change = 0
    # Loop through the list of numbers to calculate that change
    for i in range(1, len(numbers)):
        change = numbers[i] - numbers[i - 1]
        total_change += change

    if len(numbers) > 1:
        average_change = total_change / (len(numbers) - 1)
        return average_change
    else:
        return None

# To open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    sum_plcolumn = 0  # Total Profit/Losses
    row_count = 0  # Total number of rows (months)
    profit_losses = []  # List to store Profit/Losses values
    min_value = float("inf")  # Initialize minimum value to positive infinity
    max_value = float("-inf")  # Initialize maximum value to negative infinity
    min_date = ""  # Date corresponding to the minimum value
    max_date = ""  # Date corresponding to the maximum value
    column_name = "Profit/Losses"

    # Loop through each row in the CSV file
    for row in csvreader:
        row_count += 1  # Row count for each row
        profit_losses.append(int(row[column_name]))  # Add Profit/Losses value to the list
        sum_plcolumn += int(row[column_name])  # Add Profit/Losses value to the total

        # Look for the greatest increase in profits
        if int(row[column_name]) > max_value:
            max_value = int(row[column_name])
            max_date = row["Date"]

        # Look for the greatest decrease in profits
        if int(row[column_name]) < min_value:
            min_value = int(row[column_name])
            min_date = row["Date"]

    # Calculate the average change using the function
    avg_change = calculate_average_change(profit_losses)
    # Find the minimum and maximum values in the Profit/Losses column
    min_value = min(profit_losses)
    max_value = max(profit_losses)

# Print the analysis results to the terminal
print(f"Total Months: {row_count}")
print(f"Total: ${sum_plcolumn}")
print(f"Average change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_date} ${max_value}")
print(f"Greatest Decrease in Profits: {min_date} ${min_value}")

# Print the analysis results to the output text file
with open(output_file, "w") as output:
    output.write("Financial Analysis\n")
    output.write("___________________\n")
    output.write(f"Total Months: {row_count}\n")
    output.write(f"Total: ${sum_plcolumn}\n")
    output.write(f"Average change: ${avg_change:.2f}\n")
    output.write(f"Greatest Increase in Profits: {max_date} (${max_value})\n")
    output.write(f"Greatest Decrease in Profits: {min_date} (${min_value})\n")





