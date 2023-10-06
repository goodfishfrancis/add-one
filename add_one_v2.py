"""
 This script takes a excel file saved in CSV format as an input file
 and add one to each value in the first column and save the updated data 
 to an output CSV file

 Date: 10-05-2023
 Author: Alexander Solinger
"""

import csv

# Define the input and output file paths
input_file = './test_input.csv'  # Replace with the path to your input CSV file
output_file = './test_output.csv'  # Replace with the path for the output CSV file

# Open the input and output CSV files
with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_csv)

    # Process each row in the input CSV file
    for row in csv_reader:
        if row:

            # Check if the first column is numeric
            if row[0].isnumeric(): 

                # Add 1 to the first column and write the updated row to the output CSV file
                row[0] = str(int(row[0]) + 1)
                csv_writer.writerow(row)

            else: 
                print("not a number...")

print(f"Conversion complete. Output saved to {output_file}")