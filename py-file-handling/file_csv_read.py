# belajar untuk file csv

import csv

rows = []

with open("person.csv", 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # bisa dipanggil dengan for 
    # for row in csvreader:
    #    rows.append(row)
    
    # atau juga bisa dipanggil dengan list
    rows = list(csvreader)
    print("total baris : ", csvreader.line_num)

# print(rows)

for row in rows[:5]:
    print(row["first_name"] + " - " + row["email"])

