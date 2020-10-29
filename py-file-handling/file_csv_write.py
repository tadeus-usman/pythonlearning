import csv

rows = [
    {"name" : "ana", "age" : 20, "email": "ana@gmail.com"},
    {"name" : "tia", "age" : 25, "email": "tia@gmail.com"},
    {"name" : "surti", "age" : 30, "email": "surti@gmail.com"}
]

with open('data.csv', 'a') as csvfile:
    fields = ["name", "age", "email"]
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    writer.writeheader()
    writer.writerows(rows)