# import modules
import csv
import pandas as pd

# open csv file
csvfile = "03-Python_homework_PyBank_Resources_budget_data.csv"
df = pd.read_csv(csvfile)
df.columns = ["Date","Profit_Losses"]
df.head() # first five rows

x = df.Date.count() # number of entries
y = df.Profit_Losses.sum() # net amount of Profits/Losses over the entire period
z = df.Profit_Losses.diff() # date-by-date change
ave = z.mean() # average of date-by-date differences (average change)
z_min = int(z.min()) # greatest decrease in losses
z_max = int(z.max()) # greatest increase in profits
z_min_loc = df.loc[z ==z_min,"Date"].iloc[0]
z_max_loc = df.loc[z ==z_max,"Date"].iloc[0]
    
# output
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(x))
print("Total: $" + str(y))
print("Average Change: $" + str(round(ave,2)))
print("Greatest Increase in Profits: " + z_max_loc + " ($" + str(z_max) + ")")
print("Greatest Decrease in Profits: " + z_min_loc + " ($" + str(z_min) + ")")

# create new text file
f = open("PyBank.txt","w")
f.write("Financial Analysis")
f.write("\n" + "------------------------------")
f.write("\n" + "Total Months: " + str(x))
f.write("\n" + "Total: $" + str(y))
f.write("\n" + "Average Change: $" + str(round(ave,2)))
f.write("\n" + "Greatest Increase in Profits: " + z_max_loc + " ($" + str(z_max) + ")")
f.write("\n" + "Greatest Decrease in Profits: " + z_min_loc + " ($" + str(z_min) + ")")
f.close()