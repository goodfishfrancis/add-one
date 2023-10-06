"""
 This script takes a excel file saved in CSV format and adds one to each 
 value in the first column. The updated data is saved to the original file.

 Date: 10-05-2023
 Author: Alexander Solinger
"""

import csv

# Define the input file path
input_file = './test.csv'  # Replace with the path to your input CSV file

# Read the data from the input CSV file and update it in memory
with open(input_file, 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Read the data into a list of rows
    data = list(csv_reader)

# Process the data in memory and update the first column
for row in data:
    if row:
        
        # Check if the first column is numeric
        if row[0].isnumeric():  

            # Add one to the first column
            row[0] = str(int(row[0]) + 1) 
        else: 
            print("not a number...")

# Write the updated data back to the original file
with open(input_file, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the updated data to the original file
    csv_writer.writerows(data)

print(f"Update complete. Original file '{input_file}' has been modified.")

