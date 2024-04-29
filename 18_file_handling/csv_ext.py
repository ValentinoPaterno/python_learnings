"""
CSV stands for comma separated values. 
CSV is a simple file format used to store tabular data, such as a spreadsheet or database. 
CSV is a very common data format in data science.
"""
import csv
with open('./18_file_handling/csv_example.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}'
            )
            line_count += 1
    print(f'Number of lines: {line_count}')
    