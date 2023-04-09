# JSON in Python

import json

# Parse JSON - Convert from JSOn to Python

# ex JSON:
txtJSON = '{ "name":"Petch", "age":23, "city":"BKK" }'

# parse txtJSON:
parseJSON = json.loads(txtJSON)

print(parseJSON)
print(type(parseJSON))
print(parseJSON["name"])
print(parseJSON["age"])
print(parseJSON["city"])
print("----------------------")

# Convert from Python to JSON

# a Pthon object (dict):
txt = {
    "name": "tPetch",
    "age": 23,
    "city": "tBKK"
}

# convert into JSON:
conTxt = json.dumps(txt)

print(conTxt)
print(type(conTxt)) # JSON
print("----------------------")

# Format the Result

convertJson = json.dumps(txt, indent=4, separators=(". ", " = "), sort_keys=True) # change "," => ".", ":" => " = "

print(convertJson)
print("----------------------")