# import module
import csv 

# open csv file
with open("03-Python_homework_PyBank_Resources_budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) # excludes the header row for the csvreader

    # generate empty lists of Dates and Profit/Losses
    Date = []
    Profit_Loss = []
    change = []

    # populate the lists
    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(float(row[1]))
    
    # number of months
    no_months = len(Date) #86 months
    
    # net amount of profit/losses
    net_amt = sum(Profit_Loss)
    
    # average change date-by-date for profit/losses
    for i in range(1,no_months):
        # create list of date-by-date changes in profit/losses
        change.append(Profit_Loss[i] - Profit_Loss[i-1])
    ave_change = sum(change) / (no_months - 1) # there are only 85 entries for differences
    
    # greatest increase in profit
    gt_in = max(change)

    # greatest decrease in profit
    gt_dc = min(change)

    # dates corresponding to the greatest changes
    date_dc = Date[change.index(gt_dc) + 1] # to give the date for Profit_Loss[i-1]
    date_in = Date[change.index(gt_in) + 1] # to give the date for Profit_Loss[i-1]

# print out the financial analysis into text file
    print "Financial Analysis"
    print "------------------------------"
    print "Total Months: " + str(no_months)
    print "Total: $" + str(int(net_amt))
    print "Average Change: $" + str(round(ave_change,2))
    print "Greatest Increase in Profits: " + date_in + " ($" + str(int(gt_in)) + ")"
    print "Greatest Decrease in Profits: " + date_dc + " ($" + str(int(gt_dc)) + ")"