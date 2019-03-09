import os
import csv

csvpath = "C:/Users/joser/Downloads/TECMC201902DATA2-master/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

#Global variables
total_months = []
total_net = []
average_change = []

# Read in the CSV file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        #The total number of months included in the dataset
        total_months.append(row[0])
        #The net total amount of "Profit/Losses" over the entire period
        total_net.append(int(row[1]))

    #The average of the changes in "Profit/Losses" over the entire period
    for i in range(len(total_net)-1):
        average_change.append(total_net[i+1]-total_net[i])
        
#The greatest increase and decrease in profits (date and amount) over the entire period
max_increase = max(average_change)
max_decrease = min(average_change)
#Date correlation
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1 

#Print results

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_net)}")
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

#Export a text file with the results.
txt_file = "C:/Users/joser/Downloads/TECMC201902DATA2-master/02-Homework/03-Python/Instructions/PyBank/Resources/Financial_Analysis_PyBank.txt"

with open(txt_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_net)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")