# import modules
import csv

# open csv file
with open("03-Python_homework_PyPoll_Resources_election_data.csv", newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")