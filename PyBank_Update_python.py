import os
import csv

#PyBank's variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
Total_months = 0


# Directory of Current Python file
os.chdir(os.path.dirname(__file__))

# Path to collect data from the local resource folder due to CSV file was removed from my Github
budget_data_csv_path = os.path.join("C:\\Users\\ryoun\\OneDrive\\Desktop\\GT-ATL-DATA-PT-09-2020-U-C-2\\03-Python\Homework\\Instructions\\PyBank", "Resources", "budget_data.csv")


# Open and read csv file
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    
    csv_header = next(csvfile)

    
    
             
    # Read Rows in header to format months
    for row in csv_reader:

        
        count_months += 1

        
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Profit loss change
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Organize months
            months.append(row[0])

            # profit loss changes organize the changes
            profit_loss_changes.append(profit_loss_change)

            # For current profit loss
            previous_month_profit_loss = current_month_profit_loss

    
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Organize month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# PRINT TO TERMINAL
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

output_path = ('C:\\Users\\ryoun\\OneDrive\\Desktop\\GT-ATL-DATA-PT-09-2020-U-C-2\\Financial_Analysis.txt')

with open(output_path, 'w') as file:

    file.write(f"Financial Analysis")
    file.write(f"----------------------------" + "\n")
    file.write(f"Total Months:  {count_months}" + "\n")
    file.write(f"Total:  ${net_profit_loss}" + "\n")
    file.write(f"Average Change:  ${average_profit_loss}" + "\n")
    file.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})" + "\n")
    file.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})" + "\n")