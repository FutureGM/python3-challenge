import os
import csv

csvPathList = []
pybank_csvpath = os.path.join("..","pythonActivities","budget_data_1.csv")
pybank_csvpath2 = os.path.join("..", "pythonActivities", "budget_data_2.csv")

csvPathList.append(pybank_csvpath)
csvPathList.append(pybank_csvpath2)

for csvPath in csvPathList:
    with open(csvPath, newline='') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=',')

        monthlyRevenue = 0
        revenue = 0
        months = 0
        totalRevenue = 0
        totalRevenueChange = 0
        averageChange = 0
        prevRevenue = 0
        revenueChange = 0
        grtIncChange = 0
        grtDecChange = 0
        dates = []
        amount = []
        avgRevChange = []
        grtInc = []
        grtDec = []
        maxRevMonth = 0
        minRevMonth = 0
       # skip header row
        next(csvreader)
        for row in csvreader:
            revenue = row[1]
            #months.append(row[0])
            months = months + 1
            #revenue.append(row[1])
            prevRevenue = int(revenue) - prevRevenue
            #averageChange.append(row[2])
            percent = round(int(row[1]) / int(row[1]), 2)
            totalRevenue = totalRevenue + int(row[1])
            #Conditionals
            if months > 1:
               revenueChange = int(revenue) - prevRevenue
               totalRevenueChange = totalRevenueChange + revenueChange
            if revenueChange > grtIncChange:
               grtIncChange = revenueChange
               maxRevMonth = row[0]
            if revenueChange < grtDecChange:
               grtDecChange = revenueChange
               minRevMonth = row[0]
            #review_percent.append(percent)
        averageChange = round(totalRevenue/months)
        revChange = totalRevenueChange
        dates.append(months)
        amount.append(revenue)
        avgRevChange.append(totalRevenueChange)
        grtInc.append(grtIncChange)
        grtDec.append(grtDecChange)


        print("Total Months: " + str(months))
        print("Total Revenue: " + str(revenue))
        print("Average Revenue Change: " + str(averageChange))
        print("Greatest Increase in Revenue: " + maxRevMonth + str(grtInc))
        print("Greatest Decrease in Revenue: " + minRevMonth + str(grtDec))
           # Zip lists together
        budget_csv = zip(dates, amount, avgRevChange, grtInc, grtDec)
        print(budget_csv)
           # Set variable for output file
        output_file = os.path.join("..", "pythonActivities", "Budget_Analysis"+str(csvPathList.index(csvPath)+1) +".txt")

           #  Open the output file
        with open(output_file, 'w') as dataFile:
               #writer = file.writer(dataFile, delimiter= ',')

               # Write the header row
               dataFile.write("Total Months: " + str(months))
               dataFile.write('\nTotal Revenue: ' + str(revenue))
               dataFile.write('\nAverage Revenue Change: ' + str(averageChange))
               dataFile.write('\nGreatest Increase in Revenue: ' + maxRevMonth + str(grtInc))
               dataFile.write('\nGreatest Decrease in Revenue: ' + minRevMonth + str(grtDec))

               # Write in zipped rows
               #writer.writerows(budget_csv)