#import os and csv
import os
import csv
#make variable for everything 
totalMonths = 0
totalRev = 0
pastRev = 0
highestIncRev = 0
lowestDecRev = 99999999999
#create lists to store revenue change
revChange = []
#set the path to csv file 
budget_csvpath = os.path.join("Resources","budget_data.csv")
#print(budget_csvpath)
#read the csv file
with open(budget_csvpath, newline='', encoding='utf-8') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    next(budget_csvreader, None)
    for row in budget_csvreader:
        #count total months in csv file
        totalMonths +=  1
        #count total revenue in csv file
        totalRev += (int(row[1]))
        #create a variable that will count the revenue change
        monthlyRevChange = int(row[1]) - pastRev
        pastRev = int(row[1])
        #add changes in new list
        revChange.append(monthlyRevChange)
        #calculate the average change in revenue
        avgRevChange = round(sum(revChange)/totalMonths)
        #print(avgRevChange)
        #find the greatest increase in revenue
        if (monthlyRevChange > highestIncRev):
            highestIncMonth = row[0]
            highestIncRev = monthlyRevChange 
        #find the greatest decrease in revenue
        if (monthlyRevChange < lowestDecRev):
            lowestDecMonth = row[0]
            lowestDecRev = monthlyRevChange

#create varible to hold finanical analysis results and use f-strings for formatting

print("Financial Analysis")
print("----------------------------") 
print(f"Total Revenue: ${totalRev}") 
print(f"Average Revenue Change: ${avgRevChange}")
print(f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev})")
print(f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev})")

output_file = os.path.join("budget_csvpath.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Revenue: ${totalRev}\n")
    datafile.write(f"Average Revenue Change: ${avgRevChange}\n")
    datafile.write(f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev})\n")
    datafile.write(f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev})\n")