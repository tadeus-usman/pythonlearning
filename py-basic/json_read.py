
# belajar json

# JSON adalah systax untuk menyimpan dan bertukar data
# JSON adalah text, ditulis dalam Javascript object notation

# python mempunyai package json yang dapat dipakai untuk JSON

# import json module
print("import package json ------")
import json


print()
print("Parse JSON -> Convert form JSON to Python")
# bila kita punya JSON string, kita bisa parse dengan memakai json.loads() method
# dan hasilnya akan berbentuk dictionary

# contoh file JSON
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) # diubah menjadi dict

# the result is a Python dictionary:
print(y)
print(type(y))
print(y["age"])



print()
print("Convert from Python to JSON -----------")
# cara konversi dari python ke JSON menggunakan json.dump()

# a python object (dict):
x = {
    "name" : "Jhon",
    "age" : 30,
    "city" : "Jakarta"
}

#convert into JSON:
y = json.dumps(x)

# the result is a JSON string: 
print(y)
print(type(y))

# test python objects into JSON string 
print()
print("convert object Python into the JSON - Javascript equivalent ")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# exemple
print()
print("json.dumps() example -----------")
import json

x = {
    "name" : "Jhon",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "childer" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5},
        {"model" : "Ford Edge", "mpg" : 24.1},
    ]
}

# Use the indent parameter to define the numbers of indents:
# Use the separators parameter to change the default separator:

print(json.dumps(x, indent=4, separators=(". ", " = ")))
