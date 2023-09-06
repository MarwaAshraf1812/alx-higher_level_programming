#!/bin/bash

# Specify the directory where you want to create the files
directory="./"

# Define the base name for your files
base_name="file"

# Specify the range of numbers you want to use in the file names
start_number=5
end_number=34  # Adjust this based on how many files you want to create

# Loop to create the files
for ((i=start_number; i<=end_number; i++)); do
    file_name="${directory}${i}-answer.txt"  # You can change the file extension if needed
    touch "$file_name"
done

echo "$((end_number - start_number + 1)) files have been created."