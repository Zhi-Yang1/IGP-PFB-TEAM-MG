from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    day_profit = []
    for row in reader:
        day_profit.append([row[0],row[4]])

#Creating an empty list and assigning it to the variable profit_deficit
def profitlosscalc():
    """
    - This function does not accept any parameters 
    - This function checks if the net profit on the current day is lower than the previous day 
    - This function will find the difference between the current and previous day net profit if the current day net profit is lower 
    """
    filepath = Path.cwd()/"summary_report.txt"
    filepath.touch()
    # using "a" to append the data from the function to the txt file 
    with filepath.open(mode="a",encoding = "UTF-8") as file :
    # creating an empty list and assigning it to the variable profit_deficit 
        profit_deficit=[]
        # using a for loop to loop the data from the range of 1, length of the day_profit list 
        for day in range(1,len(day_profit)) :
            netprofit= int(day_profit[day-1][1])-int(day_profit[day][1])
            if int(day_profit[day][1])>int(day_profit[day-1][1])
            return 
          






