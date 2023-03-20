#Import CSV
#import os
import csv

with open("Resources/budget_data.csv") as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    #Loop Through CSV
    profits = []
    months = []

    for row in csvreader:
        profits.append(int(row[1]))
        months.append((row[0]))


    no_months = len(months) #Answer to question 1
    net = sum(profits) #Anser to question 2
    delta = []
    for i in range(1,len(profits)):
        delta.append(profits[i]-profits[i-1])
    average = sum(delta)/len(delta) #Answer to question 3
    increase = max(delta) #Anser to questions 4 & 5
    inc_index = delta.index(increase)
   
    decrease = min(delta)
    dec_index = delta.index(decrease)
with open("analysis/output.txt", "w") as f:
    print("Financial Analysis", file = f)
    print("-"*20, file = f )
    print("Total Months: ", no_months, file = f)
    print("Total: $" , net, file = f) 
    print("Average Change: ${:.2f}".format(average), file = f)
    print(f"Greatest Increase in Profits: {months[inc_index +1]} (${increase})", file = f)
    print(f"Greatest Decrease in Profits: {months[dec_index +1]} (${decrease})", file = f)

print("Financial Analysis")
print("-"*20 )
print("Total Months: ", no_months)
print("Total: $" , net) 
print("Average Change: ${:.2f}".format(average))
print(f"Greatest Increase in Profits: {months[inc_index +1]} (${increase})")
print(f"Greatest Decrease in Profits: {months[dec_index +1]} (${decrease})")

