import os
import csv
# Choosing File 1 for import selection
file_num = 1
# Pulling CSV from Certain File Path
file = os.path.join("C:\\Users\\ryoun\\OneDrive\\Desktop\\GT-ATL-DATA-PT-09-2020-U-C-2\\03-Python\Homework\\Instructions\\PyPoll", "Resources", "election_data.csv")

poll = {}

total_votes = 0

#Code to Read File for CSV
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    # Create For Loop and Exclude Rows equal to 1
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
candidates = []
num_votes = []

#Add Dictionaries For Keys
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

clean_data = list(zip(candidates, num_votes, vote_percent))

winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

#Code To Separate Ties
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#Print Fuctions for Files and File Types
output_file = os.path.join('election_results_' + str(file_num) +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')
with open(output_file, 'r') as readfile:
    print(readfile.read())