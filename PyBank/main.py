import os
import csv


# Join Current to csv file
csvpath = os.path.join("Resources","budget_data.csv")


# setup empty months list, Profit_Losses list, Profit_Changes list and Counter
Months = []
Profit_Losses = []
Profit_Changes = []
counter = 0

# open csv
with open (csvpath,newline="") as csvfile:
   # read csv
   csvreader = csv.reader(csvfile, delimiter=",")
   # remove the header of csv
   csv_header = next(csvreader)
   # Loop over to read csv and append values to predefined lists
   for row in csvreader:
        #  append to Months list from first column of data
        Months.append(row[0])
        # append to Profit_Losses list from second column of data
        Profit_Losses.append(int(row[1]))

# Loop over Profit_Losses
for row in Profit_Losses:
   # Need counter to be greater than 0 so we can retrieve two values
   if counter > 0:
       # value_1: is the value at the index before value_1
       value_1 = Profit_Losses[(counter - 1)]
       # value_2: is the value given on any iteration
       value_2 = Profit_Losses[counter]`    zzzzz
       # Calculate Monthly_Change = month2 - month1 or value_2 - value_1
       Monthly_Change = value_2 - value_1
       # Append to Profit_Changes list
       Profit_Changes.append(Monthly_Change)
       # keep adding to counter so we can step through list
       counter = counter + 1
   else:
       # add to counter, this will only happen once
       counter = counter + 1

# calculate net profits by summing up values in the list
Net = sum(Profit_Losses)

# Total Months
Total_Months = len(Months)

# Calculate Average Change and round to the nearest hundredth, used: sum(), len(), round()
Average_Change = round(sum(Profit_Changes)/len(Profit_Changes),2)

# Greatest Increase: the maximum value in the Profit_Losses list, used max()
Greatest_Increase = max(Profit_Losses)
#Greatest Decrease: the minimum value in the Profit_Losses list, used min()
Greatest_Decrease = min(Profit_Losses)

# index_1: retrive index value of Greatest_increase and store it, used ‘.index()’ method
index_1 = Profit_Losses.index(Greatest_Increase)
# index_2: retrieve index value of Greatest_decrease and store it, used ‘.index()’ method
index_2 = Profit_Losses.index(Greatest_Decrease)

# Get the values at index_1 and index_2 in Months list
Month_1 = Months[index_1]
Month_2 = Months[index_2]


#Printing the Outputs
#write to terminal
print("Financial Analysis")
print("-------------------------")
print("Total Months: $", len(Months))
print("Total Revenue: $", Net)
print("Average Revenue Change: $", Average_Change)
print("Greatest Increase in Revenue: ", Months[index_1], "($", Profit_Losses[index_1], ")")
print("Greatest Decrease in Revenue: ", Months[index_2], "($", Profit_Losses[index_2], ")")


#write to file
with open('results.txt', 'w') as results:
    #printing all the values to the given format
    print("Financial Analysis", file = results)
    print("-------------------------", file = results)
    print("Total Months: $", len(Months), file = results)
    print("Total Revenue: $", Net, file = results)
    print("Average Revenue Change: $", Average_Change, file = results)
    print("Greatest Increase in Revenue: ", Months[index_1], "($", Profit_Losses[index_1], ")", file = results)
    print("Greatest Decrease in Revenue: ", Months[index_2], "($", Profit_Losses[index_2], ")", file = results)