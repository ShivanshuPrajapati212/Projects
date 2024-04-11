import csv

word_to_count = "White"
column_index = 8
csv_filename = "adult.csv"

count = 0

with open(csv_filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[column_index] == word_to_count:
            count += 1

print(f"The word '{word_to_count}' appears {count} times in column {column_index}.")

