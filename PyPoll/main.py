import os
import csv

# Join Current to csv file
csvpath = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Create variables for calculations
candidates = []
num_votes = 0
vote_counts = []

# List of files
election_data = ['1', '2']
# open csv
with open(csvpath, newline="") as csvfile:
    # read csv
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove the header of csv
    csv_header = next(csvreader)

# Loop through files
    for files in election_data:


        # Skip headers
        line = next(csvreader,None)

        # Process the votes
        for line in csvreader:

            # Add to total number of votes
            num_votes = num_votes + 1

            # The candidate voted for
            candidate = line[2]

            # If the candidate has other votes then add to vote total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            # Else create new spot in list for candidate
            else:
                candidates.append(candidate)
                vote_counts.append(1)

    # Create variables for calculations
        percentages = []
        max_votes = vote_counts[0]
        max_index = 0

    # Percentage of vote for each candidate and the winner
        for count in range(len(candidates)):
            vote_percentage = vote_counts[count]/num_votes*100
            percentages.append(vote_percentage)
            if vote_counts[count] > max_votes:
                max_votes = vote_counts[count]
                print(max_votes)
                max_index = count
        winner = candidates[max_index]

    # Round decimal

        percentages = [round(i,2) for i in percentages]

        # Print results
        print("Election Results")
        print("--------------------------")
        print(f"Total Votes: {num_votes}")
        for count in range(len(candidates)):
            print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
        print("---------------------------")
        print(f"Winner: {winner}")



    # write to file
        with open('results.txt', 'w') as results:
            print("Election Results", file=results)
            print("--------------------------", file=results)
            print(f"Total Votes: {num_votes}", file=results)
            for count in range(len(candidates)):
                print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})", file=results)
            print("---------------------------", file=results)
            print(f"Winner: {winner}", file=results)