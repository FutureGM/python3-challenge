import os
import csv
#selecting the file
pyPoll_csvpath = os.path.join("..","python3-challenge", "election_data_1.csv")
#opening and reading the file
with open(pyPoll_csvpath, 'r', newline='') as csvFile:
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
    print("Vestal: ", vestalPct, "%" "(",vestal,")")
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
        dataFile.write("-----------------------------")
        dataFile.write("Total Votes: " + str(votesCast))
        dataFile.write("-----------------------------")
        dataFile.write("Vestal: ", vestalPct, "%" "(", vestal, ")")
        dataFile.write("Torres: ", torresPct, "%", "(", torres, ")")
        dataFile.write("Seth: ", sethPct, "%", "(", seth, ")")
        dataFile.write("Cordin: ", cordinPct, "%", "(", cordin, ")")
        dataFile.write(totVotes)
        dataFile.write(popVotes)
        dataFile.write("-----------------------------")
        dataFile.write("Winner: ", winner)
        dataFile.write("-----------------------------")
        # Write in zipped rows
        #writer.writerows(election_csv)