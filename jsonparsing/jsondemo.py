import json

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

json_data = json.dumps(person, indent=4)
print("JSON Data \n", json_data)

parsed_json = json.loads(json_data)
print(parsed_json)
print(parsed_json['age'])
