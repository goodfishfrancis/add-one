# add-one
Python scripts to iterate through the first column of csv file and update value by 1


Version 1 reads the data from the original CSV file, updates the first column values in memory, 
and then overwrites the original file with the modified data. Note that this approach directly modifies 
the original file, so one should be cautious when using it and make sure to have a backup of the data if needed. 


Version 2 reads an input CSV file, add 1 to each value in the first column, and save the updated data to a different 
output CSV file. The resulting CSV file will have the first column values incremented by 1. 
