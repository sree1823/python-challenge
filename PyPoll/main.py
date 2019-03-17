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
    khanCount = 0
    correyCount = 0
    liCount = 0
    tooleyCount = 0
    

    for row in csvreader:
        votes = votes + 1       

        if row[2] == "Khan":
           khanCount = khanCount + 1
        elif row[2] == "Correy":
            correyCount = correyCount + 1
        elif row[2] == "Li":
            liCount = liCount + 1
        else:
            tooleyStr = row[2].replace("'", "")
            tooleyCount = tooleyCount + 1
        
    print("The Total no of votes : " + str(votes))
    print ("----------------------------")
    print("Khan : " + "{:.3%}".format((khanCount/votes)) + " " + "("+str(khanCount)+")")
    print("Correy : " + "{:.3%}".format((correyCount/votes)) + " " + "("+str(correyCount)+")")
    print("Li : " + "{:.3%}".format((liCount/votes)) + " " + "("+str(liCount)+")")
    print("O'Tooley : " + "{:.3%}".format((tooleyCount/votes)) + " " + "("+str(tooleyCount)+")")
    print ("----------------------------")
    winnerCount = max(khanCount, correyCount, liCount, tooleyCount) 
    if (winnerCount == khanCount):
        winner = "Khan"
    elif (winnerCount == khanCount):
        winner = "Khan"
    elif (winnerCount == khanCount):
        winner = "Khan"
    else:
        winner = "O'Tooley"

    print ("Winner : ", winner)
    print ("----------------------------")
    

#columns = []
#with open('../../../Resources/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv','rU') as f: 
#    reader = csv.reader(f)
#    for row in reader:
#        if columns:
#            for i, value in enumerate(row):
#                columns[i].append(value)
#        else:
#            # first row
#            columns = [[value] for value in row]
# you now have a column-major 2D array of your file.
#as_dict = {c[0] : c[1:] for c in columns}


	



