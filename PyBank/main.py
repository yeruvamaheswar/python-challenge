
# This will allow us to create file paths across operating systems.
import os

# Module for reading CSV files.
import csv

# Path where the CSV file stored.
path = "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyBank/Resources"
CsvPath = os.path.join(path, 'budget_data.csv')
AllDates = []
AllAmounts = []
MonthlyProfitChange = []
TotalPL = 0
TotalMonths =0  
MaxProfitChangeIndex = 0
with open(CsvPath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)    

    # Read each row of data after the header
    for row in csvreader:
        AllDates.append(row[0])
        AllAmounts.append(int(row[1]))
    
    
    for i in range(len(AllAmounts)-1):
        MonthlyProfitChange.append(AllAmounts[i+1]-AllAmounts[i])       
    
    
    TotalMonths= len(AllDates)
    TotalPL = sum(AllAmounts)
    AvarageProfitChange = round(sum(MonthlyProfitChange)/len(MonthlyProfitChange),2)

    MaxProfitChange = max(MonthlyProfitChange)
    MaxProfitChangeIndex = MonthlyProfitChange.index(MaxProfitChange)+1
    MaxProfitMonth = AllDates[MaxProfitChangeIndex]

    MinProfitChange = min(MonthlyProfitChange)
    MinProfitChangeIndex = MonthlyProfitChange.index(MinProfitChange)+1
    MinProfitMonth = AllDates[MinProfitChangeIndex]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${TotalPL}")
    print (f"Average Change: ${AvarageProfitChange}")
    print(f"Greatest Increase in Profits: {MaxProfitMonth} (${MaxProfitChange})")
    print(f"Greatest Decrease in Profits: {MinProfitMonth} (${MinProfitChange})")
    
OutputPath= "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyBank/analysis"

AnalysisTextFile = os.path.join(OutputPath,"FinancialAnalysisReport.txt")
with open(AnalysisTextFile,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {TotalMonths}")
    file.write("\n")
    file.write(f"Total: ${TotalPL}")
    file.write("\n")
    file.write (f"Average Change: ${AvarageProfitChange}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {MaxProfitMonth} (${MaxProfitChange})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {MinProfitMonth} (${MinProfitChange})")