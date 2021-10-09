# This will allow us to create file paths across operating systems.
import os

# Module for reading CSV files.
import csv

# Path where the Input CSV file stored.
path = "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyPoll/Resources"

# Joining the path to get the full path of csv file.
CsvPath = os.path.join(path,"election_data.csv")

#Intializing Variables.
ColVoterID = []
ColCounty = []
ColCandidate=[]
PercntageList =[]
NoOfKhan =0
NoOfCorrey =0
NoOfLi =0
NoOfTooley =0

#Opening CSV file to read the items inside.
with open(CsvPath) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents.
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skiping the CSV coloumn headers.
    next(csvreader)

    # Read each row of data after the header in to a list variables.
    for row in csvreader:
        ColVoterID.append(int(row[0]))
        ColCounty.append(row[1])
        ColCandidate.append(row[2])
    
    #Assignining all the candidates to a list.
    Candidates=["Khan","Correy","Li","O'Tooley"]
    
    #Getting how many votes each candidate gets.
    for EveryCan in ColCandidate:
        if EveryCan == Candidates[0]:
            NoOfKhan += 1
        elif EveryCan == Candidates[1]:
            NoOfCorrey += 1
        elif EveryCan == Candidates[2]:
            NoOfLi += 1
        elif EveryCan == Candidates[3]:
            NoOfTooley += 1

    #All No of votes are created in to list variable.
    NoOfVotes = [NoOfKhan,NoOfCorrey,NoOfLi,NoOfTooley]
#Zipping together Candidates and there respective votes in to a dictionary.
ZipCandnVotesAsDic = dict(zip(Candidates,NoOfVotes))

#This gets the Key of a Max Value.
KeyOfMaxVoter = max(ZipCandnVotesAsDic,key=ZipCandnVotesAsDic.get)




#Getting all the voter percentages in to a list variable.
for everyNumofVotes in NoOfVotes:
    PercntageList.append(round(((everyNumofVotes/sum(NoOfVotes))*100),2))


#Printing all the Results on Terminal.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(ColVoterID)-1}")
print("-------------------------")
for x in range(len(Candidates)):
    print(f"{Candidates[x]}: {PercntageList[x]}% ({NoOfVotes[x]})")
print("-------------------------")
print(f"Winner: {KeyOfMaxVoter}")
print("-------------------------")


# Path where the Output CSV file stored.
OutputPath= "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyPoll/analysis"
# Joining the path to get the full path of csv file.
ResultsTextFile = os.path.join(OutputPath,"VoterResults.txt")

#Printing all the results on to Text file.
with open(ResultsTextFile,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(ColVoterID)}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    for x in range(len(Candidates)):
        file.write(f"{Candidates[x]}: {PercntageList[x]}% ({NoOfVotes[x]})")
        file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {KeyOfMaxVoter}")
    file.write("\n")
    file.write("-------------------------")
