
# This will allow us to create file paths across operating systems.
import os

# Module for reading CSV files.
import csv

# Path where the Input CSV file stored.
path = "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyBank/Resources"
# Joining the path to get the full path of csv file
CsvPath = os.path.join(path, 'budget_data.csv')

#Intializing Variables.
AllDates = []
AllAmounts = []
MonthlyProfitChange = []
TotalPL = 0
TotalMonths =0  
MaxProfitChangeIndex = 0

#Opening CSV file to read the items inside.
with open(CsvPath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents.
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skiping the CSV coloumn headers.
    next(csvreader)    

    # Read each row of data after the header in to a list variables.
    for row in csvreader:
        AllDates.append(row[0])
        AllAmounts.append(int(row[1]))
    
    #Apending Monthly profits.
    for i in range(len(AllAmounts)-1):
        MonthlyProfitChange.append(AllAmounts[i+1]-AllAmounts[i])       
    
    #No of months.
    TotalMonths= len(AllDates)
    #Sum of all amounts.
    TotalPL = sum(AllAmounts)
    #Avarage Profit change.
    AvarageProfitChange = round(sum(MonthlyProfitChange)/len(MonthlyProfitChange),2)

    #Calculating Maximum Profit cahnge and Maximum profit chnage month.
    MaxProfitChange = max(MonthlyProfitChange)
    MaxProfitChangeIndex = MonthlyProfitChange.index(MaxProfitChange)+1
    MaxProfitMonth = AllDates[MaxProfitChangeIndex]

    #Calculating Minimum Profit cahnge and Minimum profit chnage month.
    MinProfitChange = min(MonthlyProfitChange)
    MinProfitChangeIndex = MonthlyProfitChange.index(MinProfitChange)+1
    MinProfitMonth = AllDates[MinProfitChangeIndex]

    #Printing all the Results on Terminal.
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${TotalPL}")
    print (f"Average Change: ${AvarageProfitChange}")
    print(f"Greatest Increase in Profits: {MaxProfitMonth} (${MaxProfitChange})")
    print(f"Greatest Decrease in Profits: {MinProfitMonth} (${MinProfitChange})")

# Path where the Output CSV file stored.   
OutputPath= "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyBank/analysis"
# Joining the path to get the full path of csv file.
AnalysisTextFile = os.path.join(OutputPath,"FinancialAnalysisReport.txt")
#Printing all the results on to Text file.
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