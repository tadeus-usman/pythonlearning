import json

with open("person.json", "r") as personfile:
    data = json.load(personfile)

    for person in data["person"]:
        # print(person)
        age = person["age"]
        print(person["name"] +"-" , age ,"-"+ person["email"] )
