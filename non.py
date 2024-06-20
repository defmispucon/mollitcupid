import json

json_string = '{"Name": "Jennifer Smith", "Contact Number": 7867567898, "Email": "jen123@gmail.com", "Hobbies":["Reading", "Sketching", "Horse Riding"] }'
python_object = json.loads(json_string)

print(python_object)
