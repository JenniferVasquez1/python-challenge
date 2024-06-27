import csv
import os

#loading the files to read and write from
budget_data_csv = os.path.join("Resources","budget_data.csv")
budget_data_txt = os.path.join("analysis","budget_data.txt")

#creating variable to read the budget
totalMonths = 0
totalnet = 0
monthofchange = []
changelist = []
greatestincrease = ["", 0]
greatestdecrease =["", 9999999999]

#reading csv file and calculatig requirements
with open(budget_data_csv) as data:
    reader = csv.reader(data)
     
    heading = next(reader)

    rowone = next(reader)
    totalMonths += 1
    totalnet += int(rowone[1])
    previousnet = int(rowone[1])

    for row in reader:
        totalMonths += 1
        netchange = int(row[1]) - previousnet
        changelist += [netchange]
        monthofchange += row[0]
        

        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange

        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange

monthlyaverage = sum(changelist)/len(changelist)

FinancialAnalysis=(
        f"Financial Analysis \n"
        f"---------------------------------------------------- \n"
        f"Total Months: {totalMonths} \n"
        f"Total: {totalnet} \n"
        f"Monthly Average: {monthlyaverage} \n"
        f"Greatest Increase: {greatestincrease[0]} (${greatestincrease[1]}) \n"
        f"Greatest Decrease: {greatestdecrease[0]} (${greatestdecrease[1]}) \n"
)
print(FinancialAnalysis)

with open(budget_data_txt,"w") as txt_file:
    txt_file.write(FinancialAnalysis)
