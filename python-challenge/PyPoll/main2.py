import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("/Users/gwendolinegrenu/Desktop/Starter_Code-4/PyPoll/Resources/election_data.csv")
# Define the output text file name
output_file = "vote_counting.txt"

# Create an empty list to store the votes
votes = []

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Loop through each row in the CSV file and add the candidate's name to the votes list
    for row in csvreader:
        votes.append(row["Candidate"])

    # Print the header for the election results
    print("Election results")
    print("--------------------")
    print("Total votes:", len(votes))
    print("--------------------")

# Function to analyze the votes and calculate results
def analyze_vote(votes):
    # Create a dictionary to store candidate votes
    candidate_votes = {}

    # Count the votes for each candidate
    for candidate in votes:
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    
    total_votes = len(votes)
    
    # Calculate the percentage of votes for each candidate and create a new dictionary to store the results
    candidate_percentages = {}
    for candidate, votes_received in candidate_votes.items():
        candidate_percentages[candidate] = (votes_received / total_votes) * 100
    
    # Determine the winner based on the maximum votes received
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the candidate votes and percentages
    for candidate, percentage in candidate_percentages.items():
        print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]} votes)")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    
    # Prepare the result output for the text file as a list of strings
    result_output = []

    result_output.append("Election results")
    result_output.append("--------------------")
    result_output.append(f"Total votes: {len(votes)}")
    result_output.append("--------------------")

    for candidate, percentage in candidate_percentages.items():
        result_output.append(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]} votes)")
    
    result_output.append("-------------------------")
    result_output.append(f"Winner: {winner}")
    result_output.append("-------------------------")

    return "\n".join(result_output)

# Analyze the votes using the defined function
results = analyze_vote(votes)

# Write the analysis results to the output text file
with open(output_file, "w") as output:
    output.write(results)


    
