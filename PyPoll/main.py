import os
import csv

path = "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyPoll/Resources"

CsvPath = os.path.join(path,"election_data.csv")
ColVoterID = []
ColCounty = []
ColCandidate=[]
PercntageList =[]
NoOfKhan =0
NoOfCorrey =0
NoOfLi =0
NoOfTooley =0
with open(CsvPath) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    for row in csvreader:
        ColVoterID.append(int(row[0]))
        ColCounty.append(row[1])
        ColCandidate.append(row[2])
    #def Unique(list):
        
    Candidates=["Khan","Correy","Li","O'Tooley"]
    
    for EveryCan in ColCandidate:
        if EveryCan == Candidates[0]:
            NoOfKhan += 1
        elif EveryCan == Candidates[1]:
            NoOfCorrey += 1
        elif EveryCan == Candidates[2]:
            NoOfLi += 1
        elif EveryCan == Candidates[3]:
            NoOfTooley += 1


    NoOfVotes = [NoOfKhan,NoOfCorrey,NoOfLi,NoOfTooley]

ZipCandnVotesAsDic = dict(zip(Candidates,NoOfVotes))

KeyOfMaxVoter = max(ZipCandnVotesAsDic,key=ZipCandnVotesAsDic.get)





for everyNumofVotes in NoOfVotes:
    PercntageList.append(round(((everyNumofVotes/sum(NoOfVotes))*100),2))



print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(ColVoterID)-1}")
print("-------------------------")
for x in range(len(Candidates)):
    print(f"{Candidates[x]}: {PercntageList[x]}% ({NoOfVotes[x]})")
print("-------------------------")
print(f"Winner: {KeyOfMaxVoter}")
print("-------------------------")


OutputPath= "/Users/mr7macbookpro/Documents/DAV BC/HomeWork/3. PythonChallenge/python-challenge/PyPoll/analysis"

ResultsTextFile = os.path.join(OutputPath,"VoterResults.txt")
with open(ResultsTextFile,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(ColVoterID)-1}")
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
