'''import json

data = {
    "name": "Abdulloh",
    "surname": "Abdulloh",
    "age": 20
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)'''
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)