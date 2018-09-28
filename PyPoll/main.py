import csv

# function for number of voters
def voter_counter(votes_list):
    num = 0
    for each in votes_list:
        num = num + 1
    return num    

# function to find unique candidates
def unique_candidates (votes_list):
    tally = [i[2] for i in votes_list] # list of candidates
    unique = {}
    for i in tally:
        if not i in unique: 
            unique[i] = 1
        else:
            unique[i] += 1
    return unique

# calculate percent votes per candidate
def pct_votes(votes_list):
    values = unique_candidates(votes_list).values()
    pct = [((float(i) / voter_counter(votes_list)) * 100) for i in values]
    return pct

###
# open csv file
with open("03-Python_homework_PyPoll_Resources_election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader,None)

    # create a list to be used in the function/s
    votes = [row for row in csvreader]

    #summarise
    total_votes = voter_counter(votes)
    cand_votes = unique_candidates(votes).values()
    cand_keys = unique_candidates(votes).keys()
    cand_pct = pct_votes(votes)
    win = max(pct_votes(votes))

    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------")

    election_results = [[x,y,z] for x,y,z in zip(cand_keys, cand_pct, cand_votes)]
    for row in election_results:
        print(row[0] +": " + str(round(row[1],3)) + "% (" + str(row[2]) + ")")

        if row[1] == win:
            winner = row[0]

    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")