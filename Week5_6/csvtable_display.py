'''
This program reads a CSV file and display its contents in a tabular format.
'''
import csv
with open('kohli_ipl.csv','r') as f:
    content = csv.reader(f)
    rows = list(content)
    if rows:
        col_wid = [max(len(item) for item in col) for col in zip(*rows)]

        for row in rows:
            formatted_row = " | ".join(item.ljust(col_wid[i]) for i, item in enumerate(row))
            print(formatted_row)
    else:
        print("Empty file.")