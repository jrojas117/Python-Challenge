import os
import csv

csvpath = "C:/Users/joser/Downloads/TECMC201902DATA2-master/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

#Global variables
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        #The total number of votes cast
        total_votes +=1
        #Count the votes for each candidate
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1


#Create a list with the results and a list with the candidate. This will help us to create a dictionary and extract winner with name
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]
#Create dictionary
dictionary_votes = dict(zip(candidates,votes))
#Extract winner with name
winner = max(dictionary_votes, key=dictionary_votes.get)

#Calculate percentage for each candidate
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

#Export a text file with the results.
txt_file = "C:/Users/joser/Downloads/TECMC201902DATA2-master/02-Homework/03-Python/Instructions/PyPoll/Resources/Elections_Data_PyPoll.txt"

with open(txt_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")