# Importing the File
import csv

# Files Input and Output Paths
Input_Path = r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyBank\Resources\budget_data.csv"
Output_Path = r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyBank\Analysis\Analysis_Text.txt"

# File Path
csv_path = r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyBank\Resources\budget_data.csv"

# Initial value of the variables
Total_Months = 0
Total = 0
Changes = []
Dates = []
# Openning the CSV file and reading the data
with open(csv_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(csv_reader)

    # Looping through each row in the CSV file
    for row in csv_reader:
        # Counting the number of months and add to the total
        Total_Months += 1
        Total += int(row[1])

        # Stores the monthly changes and dates
        if Total_Months > 1:
            Changes.append(int(row[1]) - prev_value)
            Dates.append(row[0])
        prev_value = int(row[1])

# Calculating the average monthly change
AverageChanges = sum(Changes) / len(Changes)

# Finding the index of the max and min changes
max_index = Changes.index(max(Changes))
min_index = Changes.index(min(Changes))

# Finding the dates corresponding to the max and min changes
Greatest_Increase_Date = Dates[max_index]
Greatest_Decrease_Date = Dates[min_index]

# Printing the results (Exporting to the terminal)
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(Total_Months))
print("Total: $" + str(Total))
print("Average Change: $" + str(round(AverageChanges, 2)))
print("Greatest Increase in Profits: " +
      Greatest_Increase_Date + " ($" + str(max(Changes)) + ")")
print("Greatest Decrease in Profits: " +
      Greatest_Decrease_Date + " ($" + str(min(Changes)) + ")")

# Exporting a text file with the analysis results
with open(Output_Path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {Total_Months}\n")
    output_file.write(f"Total: ${Total}\n")
    output_file.write(f"Average Change: ${AverageChanges:.2f}\n")
    output_file.write(
        f"Greatest Increase in Profits: {Greatest_Increase_Date} (${max(Changes)})\n")
    output_file.write(
        f'Greatest Decrease in Profits: {Greatest_Decrease_Date} (${min(Changes)})\n')
