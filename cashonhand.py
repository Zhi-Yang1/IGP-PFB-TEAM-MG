from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    day_cashonhand = []
    for row in reader:
        day_cashonhand.append([row[0],row[1]])
        
# creating a function to calculate the difference in cash on hand if the cash on hand on the current day is lesser than that of the previous day
def cashonhandcalc():
        """
    - This function does not accept any parameters 
    - This function checks if the cash on hand on the current day is lower than the previous day 
    - This function will find the difference between the current and previous day cash on hand if the current day cash on hand is lower 
    """
        filepath = Path.cwd()/"summary_report.txt"
        filepath.touch()
        # using mode="a" to append into the txt file 
        with filepath.open(mode="a",encoding = "UTF-8") as file :
    # creating an empty list and assigning it to the variable cash_deficit 
            cash_deficit=[]
            # using a for loop to loop the data from the range of 1, length of the day_cashonhand list 
            for day in range(1,len(day_cashonhand)):
                # calculating the cash on hand if the current day's cash on hand is lower than that of the previous day
                cash=int(day_cashonhand[day-1][1])- int(day_cashonhand[day][1])
                # using if to check if the cash on hand on the current day is higher and if the difference is more than 0
                if int(day_cashonhand[day][1]) > int(day_cashonhand[day-1][1]) and cash > 0:
                    # return the cash surplus statement
                    return "CASH ON HAND ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                # checking if the cash on hand on the current day is more than that of the previous day
                elif int(day_cashonhand[day][1]) < int(day_cashonhand[day-1][1]): 
                    # assigning the day to the variable day_num 
                    day_num = day_cashonhand[day][0]
                    # appending the day and calculated cash on hand amount into the empty cash_deficit list
                    cash_deficit.append([day_num,cash])
                    # using a for loop to loop the day and amount data from the cash deficit list 
                    for day, amount in cash_deficit : 
                        # writing the cash on hand statement into the txt file 
                        file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
cashonhandcalc()

                   
            
