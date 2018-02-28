import os
import csv
#selecting the file
csvPathList = []
csvPathList_2 = []
pyPoll_csvpath = os.path.join("..","python3-challenge", "election_data_1.csv")
pyPoll_csvpath2 = os.path.join("..","python3-challenge", "election_data_2.csv")

csvPathList.append(pyPoll_csvpath)
csvPathList_2.append(pyPoll_csvpath2)
#opening and reading the file
with open(pyPoll_csvpath, 'r', newline="") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    votesCast = 0
    vestal = 0
    torres = 0
    seth = 0
    cordin = 0
    vestalPct = 0
    torresPct = 0
    sethPct = 0
    cordinPct = 0
    winner = 0
    pctVotes1 = []
    pctVotes2 = []
    pctVotes3 = []
    pctVotes4 = []
    candidate1 = []
    candidate2 = []
    candidate3 = []
    candidate4 = []
    totVotes = []
    popVotes = []
# skip header row
    next(csvreader)
    for row in csvreader:
    #assign values to each variable
        votesCast = votesCast + 1
    #conditionals for voters per candidate & percent
        if row[2] == "Vestal":
            vestal = vestal + 1
            vestalPct = round(float(vestal/votesCast) * 100)
        if row[2] == "Torres":
            torres = torres + 1
            torresPct = round(float(torres / votesCast) * 100)
        if row[2] == "Seth":
            seth = seth + 1
            sethPct = round(float(seth / votesCast) * 100)
        if row[2] == "Cordin":
            cordin = cordin + 1
            cordinPct = round(float(cordin / votesCast) * 100)

    #print(row[2])
        if vestal > torres or vestal > seth or vestal > cordin:
            winner = "Vestal", vestal
        elif torres > vestal or torres > seth or torres > cordin:
            winner = "Torres",torres
        elif seth > vestal or seth > torres or seth > cordin:
            winner = "Seth", seth
        else:
            winner = "Cording", cordin
    # append each value
    pctVotes1.append(vestalPct)
    pctVotes2.append(torresPct)
    pctVotes3.append(sethPct)
    pctVotes4.append(cordinPct)
    totVotes.append(votesCast)
    candidate1.append(vestal)
    candidate2.append(torres)
    candidate3.append(seth)
    candidate4.append(cordin)
    popVotes.append(winner)

# print statements
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(votesCast))
    print("-----------------------------")
    print("Vestal: ", vestalPct, "%", "(",vestal,")")
    print("Torres: ", torresPct, "%", "(",torres,")")
    print("Seth: ", sethPct, "%", "(",seth,")")
    print("Cordin: ", cordinPct, "%", "(", cordin, ")")
    print(totVotes)
    print(popVotes)
    print("-----------------------------")
    print("Winner: ",winner)
    print("-----------------------------")

    election_csv = zip(totVotes, pctVotes1, pctVotes2, pctVotes3, pctVotes4, candidate1, candidate2, candidate3, candidate4, popVotes)
    print(election_csv)
# Set variable for output file
    output_file = os.path.join("..", "python3-challenge", "Election_Results.txt")

#  Open the output file
    with open(output_file, 'w') as dataFile:
        writer = csv.writer(dataFile, delimiter=',')

    # Write the header row
        dataFile.write
        dataFile.write("Election Results")
        dataFile.write("\n-----------------------------")
        dataFile.write("\nTotal Votes: " + str(votesCast))
        dataFile.write("\n-----------------------------")
        dataFile.write("\nVestal: " + str(vestalPct) + "%" + "(" + str(vestal) + ")")
        dataFile.write("\nTorres: " + str(torresPct) +  "%" + "(" + str(torres) + ")")
        dataFile.write("\nSeth: " + str(sethPct) + "%" + "(" + str(seth) + ")")
        dataFile.write("\nCordin: " + str(cordinPct) + "%" + "(" + str(cordin) + ")")
        dataFile.write("\n" + str(totVotes))
        dataFile.write("\n" + str(popVotes))
        dataFile.write("\n-----------------------------")
        dataFile.write("\nWinner: " + str(winner))
        dataFile.write("\n-----------------------------")
with open(pyPoll_csvpath2, 'r', newline="") as csvFile_2:
    csvreader_2 = csv.reader(csvFile_2, delimiter=",")
    votes_Cast = 0
    khan = 0
    correy = 0
    li = 0
    oTooley = 0
    khanPct = 0
    correyPct = 0
    liPct = 0
    oTooleyPct = 0
    winner_2 = 0
    pctVotes_1 = []
    pctVotes_2 = []
    pctVotes_3 = []
    pctVotes_4 = []
    candidate_1 = []
    candidate_2 = []
    candidate_3 = []
    candidate_4 = []
    tot_Votes = []
    pop_Votes = []

# skip header row
    next(csvreader_2)
    for row_2 in csvreader_2:
        # assign values to each variable
        votes_Cast = votes_Cast + 1
        # conditionals for voters per candidate & percent
        if row_2[2] == "Khan":
            khan = khan + 1
            khanPct = round(float(khan / votes_Cast) * 100)
        if row_2[2] == "Correy":
            correy = correy + 1
            correyPct = round(float(correy / votes_Cast) * 100)
        if row_2[2] == "Li":
            li = li + 1
            liPct = round(float(li / votes_Cast) * 100)
        if row_2[2] == "O'Tooley":
            oTooley = oTooley + 1
            oTooleyPct = round(float(oTooley / votes_Cast) * 100)
        # print(row[2])
        if khan > correy or khan > li or khan > oTooley:
            winner_2 = "Khan", khan
        elif correy > khan or correy > li or correy > oTooley:
            winner_2 = "Correy", correy
        elif li > khan or li > correy or li > oTooley:
            winner_2 = "Li", li
        else:
            winner_2 = "O'Tooley", oTooley
    pctVotes_1.append(khanPct)
    pctVotes_2.append(correyPct)
    pctVotes_3.append(liPct)
    pctVotes_4.append(oTooleyPct)
    tot_Votes.append(votes_Cast)
    candidate_1.append(khan)
    candidate_2.append(correy)
    candidate_3.append(li)
    candidate_4.append(oTooley)
    pop_Votes.append(winner_2)
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(votes_Cast))
print("-----------------------------")
print("Khan: ", khanPct, "%" "(", khan, ")")
print("Correy: ", correyPct, "%", "(", correy, ")")
print("Li: ", liPct, "%", "(", li, ")")
print("O'Tooley: ", oTooleyPct, "%", "(", oTooley, ")")
print(tot_Votes)
print(pop_Votes)
print("-----------------------------")
print("Winner: ", winner_2)
print("-----------------------------")

election_csv_2 = zip(tot_Votes, pctVotes_1, pctVotes_2, pctVotes_3, pctVotes_4, candidate_1, candidate_2, candidate_3,
                   candidate_4, pop_Votes)
print(election_csv_2)
# Set variable for output file
output_file_2 = os.path.join("..", "python3-challenge", "Election_Results_2.txt")

#  Open the output file
with open(output_file_2, 'w') as dataFile_2:
    writer_2 = csv.writer(dataFile_2, delimiter=',')

    # Write the header row
    dataFile_2.write
    dataFile_2.write("Election Results")
    dataFile_2.write("\n-----------------------------")
    dataFile_2.write("\nTotal Votes: " + str(votes_Cast))
    dataFile_2.write("\n-----------------------------")
    dataFile_2.write("\nKhan: " + str(khanPct) + "% " + "(" + str(khan) + ")")
    dataFile_2.write("\nCorrey: " + str(correyPct) + "% " + "(" + str(correy) + ")")
    dataFile_2.write("\nLi: " + str(liPct) + "% " + "(" + str(li) + ")")
    dataFile_2.write("\nO'Tooley: " + str(oTooleyPct) + "% " + "(" + str(oTooley) + ")")
    dataFile_2.write("\n" + str(tot_Votes))
    dataFile_2.write("\n" + str(pop_Votes))
    dataFile_2.write("\n-----------------------------")
    dataFile_2.write("\nWinner: " + str(winner_2))
    dataFile_2.write("\n-----------------------------")
    # Write in zipped rows
    #writer.writerows(election_csv)