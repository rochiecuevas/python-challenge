# import modules
import csv

print("Election Results")
print("----------------------------")

# open csv file
with open("03-Python_homework_PyPoll_Resources_election_data.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    next(csvreader,None)

    Poll_Results = [] # start with an empty set
    for row in csvreader:
        Poll_Results.append(row) # populate the list with dictionaries of voter-county-candidate combinations
    
    no_voters = len(Poll_Results) # number of voters

    print("Total Votes: " + str(no_voters))
    print("----------------------------")

    Candidate = [] # empty list
    for vote in Poll_Results: # populate the empty list of candidates
        Candidate.append(vote["Candidate"])
    
    candidate_set = set(Candidate) # list of candidates

    cand_vote = [] # empty list
    for i in candidate_set:
        cand_vote.append(Candidate.count(i)) # populate list of the number of votes per candidate

    pct_vote = [] # empty list    
    for j in cand_vote:    
        pct_vote.append((float(j) / no_voters) * 100) # populate list of % votes per candidate
    
    win = max(pct_vote)

    # create a zip file of the lists
    election_results = [[x,y,z] for x,y,z in zip(candidate_set,pct_vote,cand_vote)]

    # find the winning candidate
    for row in election_results:
        summary = row[0] + ": " + str(row[1]) +"%" + " (" + str(row[2]) + ")"
        print(summary)
        
        if row[1] == win:
            winner = row[0] 
    
    print("----------------------------")
    print("Winner: " + winner)
    print("----------------------------")

        