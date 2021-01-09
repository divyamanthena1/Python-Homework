import pathlib
import csv

csvpath = pathlib.Path('budget_data.csv')


months = []
profit = []
change = []
sum_profit = 0
greatest = 0
least = 0
average_change = 0



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        sum_profit += int(row[1])


for i in range(1, len(profit)):
    p = profit[i] - profit[i-1]
    change.append(p)

for i in range(len(change)):
    average_change += change[i]
    if change[i] > greatest:
        greatest = change[i]
        greatest_month = months[i+1]
    if change[i] < least:
        least = change[i]
        least_month = months[i+1]
   

average_change /= (len(months)-1)
    
print("Financial Analysis")
print()
print("Total Months: ")
print(len(months))
print()
print("Total: ")
print(sum_profit)
print()
print("Average Change: ")
print(average_change)
print()
print("Greatest Increase in Profits: ")
print(greatest_month) 
print(greatest)
print()
print("Greatest Decrease in Profits: ")
print(least_month)
print(least)
print()

import sys
f = open("budget.out", 'w')
sys.stdout = f
print("Financial Analysis")
print()
print("Total Months: ")
print(len(months))
print()
print("Total: ")
print(sum_profit)
print()
print("Average Change: ")
print(average_change)
print()
print("Greatest Increase in Profits: ")
print(greatest_month) 
print(greatest)
print()
print("Greatest Decrease in Profits: ")
print(least_month)
print(least)
print()
f.close()

