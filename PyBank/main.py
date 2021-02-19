# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


import csv

with open("./Resources/budget_data.csv", "r") as budget_data:
    clean_data = csv.reader(budget_data)
    header_row = next(clean_data)
    # print (list(clean_data))
    for row in clean_data:
        print (row)