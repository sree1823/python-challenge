import os

import csv
from collections import defaultdict


csvpath = os.path.join('../../..', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

print ("Election Results")
print ("----------------------------")
with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler, delimiter=',')
    header = next(csvreader)
    votes = 0

    #for row in csvreader:
    #    votes = votes + 1
    #print("The Total no of votes : " + str(votes))
    #print ("----------------------------")

columns = []
with open('../../../Resources/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv','rU') as f: 
    reader = csv.reader(f)
    for row in reader:
        if columns:
            for i, value in enumerate(row):
                columns[i].append(value)
        else:
            # first row
            columns = [[value] for value in row]
# you now have a column-major 2D array of your file.
as_dict = {c[0] : c[1:] for c in columns}


	



