# Importing CSV File
import csv

# Files Input and Output Paths
Input_Path = r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyPoll\Resources\election_data.csv"
Output_Path = r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyPoll\Analysys\Analysys_Text.txt"

# Openning the file and reading
with open(r"D:\Ohana - Data Analysis Bootcamp\Classwork\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\02-Homework\03-Python\python-challenge\PyPoll\Resources\election_data.csv") as file:
    reader = csv.reader(file)
    next(reader)
# Setting the first initial value to Total Votes and creating empty dict to store values
    Total_Votes = 0
    Candidates = {}
    Percentage = {}

# Looping trough each row in the CSV file
    for row in reader:
        Total_Votes = Total_Votes + 1
        Candidate = row[2]
        if Candidate not in Candidates:
            Candidates[Candidate] = 1
        else:
            Candidates[Candidate] += 1
        for Candidate, votes in Candidates.items():
            Percentage[Candidate] = (votes / Total_Votes) * 100
    winner = max(Candidates, key=Candidates.get)

# Printing the Output to the terminal
    print("Elections Results")
    print("----------------------")
    print(f"Total Votes: {Total_Votes}")
    print("----------------------")

# Printing the output looping through each key value to the terminal
    for Candidate, votes in Candidates.items():
        print(f"{Candidate}: {Percentage[Candidate]:.3f}% ({votes})")
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")

# Exporting a text file that contains the results from the analysis
with open(Output_Path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {Total_Votes}\n")
    output_file.write("-------------------------\n")
    for Candidate, votes in Candidates.items():
        output_file.write(
            f"{Candidate}: {Percentage[Candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
