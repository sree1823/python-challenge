#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os

import csv

csvpath = os.path.join('../../..', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

print ("Financial Analysis")
print ("----------------------------")


with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler, delimiter=',')
    header = next(csvreader)
    month = 0
    net = 0

    
    for row in csvreader:
        month = month + 1
        net = net + int(row[1])
    print("The Total months : " + str(month))
    print("Total : " + str(net))

    
