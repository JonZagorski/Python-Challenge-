#import the important things 
import os 
import csv 

#variables to store values go here 
totalvotes = 0
number_votes = 0
#make a list to store candidates
candidates = []
#make list for vote counts
vote_counts =[]

#set the path to election_data 
election_data = os.path.join("resources","election_data.csv")

#open election_data 
with open(election_data, newline='', encoding= 'utf-8') as csvfile:
    #read csvfile
    election_csvreader = csv.reader(csvfile,delimiter=',')
    #skip header line
    next(election_csvreader, None)
    #start for loop
    for row in election_csvreader:
        #count the total rows
        totalvotes += 1

        #set candidate list with row[2] values 
        candidate = row[2]

        #add the votes to candidates
        if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #add each candidate to the list 
        else:
            candidates.append(candidate)
            vote_counts.append(1)
    
    
    pct = []
    max_votes = vote_counts[0]
    max_index = 0

    for x in range(len(candidates)):
        #calculation to get the percentage, x is the looper value
        vote_pct = round(vote_counts[x]/totalvotes*100, 2)
        pct.append(vote_pct)
    
        if vote_counts[x] > max_votes:
            max_votes = vote_counts[x]
            max_index = x

    winner = candidates[max_index] 


#Test the variables
#print(totalvotes)
#print(candidates)
#print(vote_counts)
#print(max_votes)
#print(election_winner)

print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {totalvotes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {pct[x]}% ({vote_counts[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #Export file name and open as text file
output_file = os.path.join("election_results.txt")
with open(output_file, "w", newline="") as datafile:

    
    # Write results to export text file
    datafile.write("Election Results\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Total Votes:  {number_votes}\n")
    datafile.write("-----------------------------\n")
    for count in range(len(candidates)):
        datafile.write(f"{candidates[count]}: {pct[count]}% ({vote_counts[count]})\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Winner:  {winner}\n")
    datafile.write("-----------------------------\n")