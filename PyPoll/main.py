# Steps
# 1. Read csv 1 & 2 and iterate through the data to create the candidate list and count the votes for each candidate
# 2. Maintain 2 lists: 1 each for candidate name and his/her votes. Keep incrementing vote count the list for vote counts. Maintain the same index for the corresponding value in both the lists.
# 3. Create a text file (PollResults.txt) and print the results in specified format into the same.
# 4. Open the file and print the content on the terminal

#import the required modules
import csv

#open the csv files and using csv reader method create the list objects to iterate through the data
with open('./election_data_1.csv', 'r') as wb1:
  reader1 = csv.reader(wb1)
  wb1_list = list(reader1)
with open('./election_data_2.csv', 'r') as wb2:
  reader2 = csv.reader(wb2)
  wb2_list = list(reader2)

#creating blank list to store candidate names & corresponding votes.
canList = []
voteCt = []
    
#iterating through the data of 'election_data_1.csv' and adding the Candidate Names and corresponding vote count into the respective lists
for i in range(1,len(wb1_list)):
    if wb1_list[i][2] not in canList:
        canList.append(wb1_list[i][2])
#        print("Added ", wb1_list[i][2] , ' at Index ', canList.index(wb1_list[i][2]))
        voteCt.append(1)
    elif wb1_list[i][2] in canList:
        voteCt[canList.index(wb1_list[i][2])] = voteCt[canList.index(wb1_list[i][2])] + 1

#iterating through the data of 'election_data_2.csv' and adding the Candidate Names and corresponding vote count into the respective lists
for j in range(1,len(wb2_list)):
    if wb2_list[j][2] not in canList:
        canList.append(wb2_list[j][2])
#        print("Added ", wb2_list[j][2] , ' at Index ', canList.index(wb2_list[j][2]))
        voteCt.append(1)
    elif wb2_list[j][2] in canList:
        voteCt[canList.index(wb2_list[j][2])] = voteCt[canList.index(wb2_list[j][2])] + 1

# print("Final Cand List: " , canList)
# print("Final Vote List: " , voteCt)
# print("Max vote count is: " , max(voteCt), " and it is for candidate: ", canList[voteCt.index(max(voteCt))])

#assigning total vote count into a variable for further use
totVotes = sum(voteCt)

#create a text file and write the results into it.
with open("./PollResults.txt", "w") as text_file:
    print(f"=======================================", file=text_file)
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {totVotes}", file=text_file)
    print(f"-------------------------", file=text_file)
    for k in range(len(canList)):
        print(f"{canList[k]} : {round((voteCt[k]/totVotes * 100),1)}% ({voteCt[k]})", file=text_file )
    print(f"-------------------------", file=text_file)
    print(f"Winner: {canList[voteCt.index(max(voteCt))]}", file=text_file)
    print(f"=======================================", file=text_file)

#read the results from text file and print it on the terminal
with open("./PollResults.txt", "r") as f:
  lineArr=f.read().split('\n')
  for line1 in lineArr:
    print(line1)
