import csv

with open ("Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    results = {}
    for row in csvreader: 
        candidate = row[2]
        if candidate in results.keys():
            results[candidate] += 1 
        else: 
            results[candidate] = 1

#print(results.items())
total_votes = sum(results.values())
winner = sorted(results.items(), key = lambda  x: x[1])[-1]
with open("analysis/output.txt", "w") as f:
    print("Election Results", file = f)
    print("-"*20, file = f )
    print("Total Votes: ", total_votes, file = f)
    print("-"*20, file = f )
    for key,val in results.items():
        print(f"{key}: {(val/total_votes) * 100:.3f}% ({val})", file = f)
    print("-"*20, file = f )
    print("Winner: ", winner[0], file =f)
    print("-"*20, file = f )

print("Election Results")
print("-"*20 )
print("Total Votes: ", total_votes)
print("-"*20 )
for key,val in results.items():
        print(f"{key}: {(val/total_votes) * 100:.3f}% ({val})")
print("-"*20 )
print("Winner: ", winner[0])
print("-"*20 )