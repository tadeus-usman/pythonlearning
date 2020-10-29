# belajar JSON

import json

data = {}

data["person"] = [
    {"name" : "ana", "age" : 20, "email": "ana@gmail.com"},
    {"name" : "tia", "age" : 25, "email": "tia@gmail.com"},
    {"name" : "surti", "age" : 30, "email": "surti@gmail.com"}
]

with open("person.json", "w") as personfile:
    json.dump(data, personfile)
