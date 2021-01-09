import pathlib
import csv
import pandas as pd

csvpath = pathlib.Path('election_data.csv')


votes = []
candidate = []
khan = 0
correy = 0
li = 0
ot = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[0])
        candidate.append(row[2])
        if(row[2] == "Khan"):
            khan +=1
        if(row[2] == "Correy"):
            correy +=1
        if(row[2] == "Li"):
            li +=1
        if(row[2] == "O'Tooley"):
            ot +=1

print("Election Results")       
print("Total Votes")       
print(len(votes))
print("Candidates")
   

candidate_dict = {
    "Candidate Name": ["Khan","Correy","Li","O'Tooley"],
    "Percent Won": [khan/len(candidate), correy/len(candidate), li/len(candidate), ot/len(candidate)],
    "Number of Votes": [khan, correy, li, ot]
}


print(candidate_dict)
print("Winner: ")
if(max(khan,correy,li,ot) == khan):
    print("Khan") 
elif(max(khan,correy,li,ot) == correy):
    print("Correy") 
elif(max(khan,correy,li,ot) == li):
    print("Li") 
else:
    print("O'Tooley")

import sys
f = open("election.out", 'w')
sys.stdout = f
print("Election Results")       
print("Total Votes")       
print(len(votes))
print("Candidates")
print(candidate_dict)
print("Winner: ")
if(max(khan,correy,li,ot) == khan):
    print("Khan") 
elif(max(khan,correy,li,ot) == correy):
    print("Correy") 
elif(max(khan,correy,li,ot) == li):
    print("Li") 
else:
    print("O'Tooley")
f.close()