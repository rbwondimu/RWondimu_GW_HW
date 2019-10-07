# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources/election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:
            total_candidates = row[2]        

        if row[2] not in candidate_options:
            
            candidate_options.append(row[2])

            candidate_votes[row[2] = 1
            
        else:
            candidate_votes[row[2]] = candidate_votes[row["Candidate"]] + 1

    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


with open(file_to_output, "w") as txt_file:

    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = # YOUR CODE HERE. HINT: Print the `candidate`, a formatted version of `vote_percentage`, as well as the number of `votes`
        f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

with open(file_to_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))    


