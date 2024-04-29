"""
JSON stands for JavaScript Object Notation. 
Actually, it is a stringified JavaScript object or Python dictionary.
"""
# Example
# - Dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# - JSON: A str form dictionary
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# JSON to Dictionary
import json
person_json = '''{
    "name":"Valentino",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct["name"])

# Dictionary to JSON
person = {
    "name": "valentino",
    "country": "argentina",
    "city": "corrientes",
    "skills": [
        "Python",
        "Django"
    ]
}
print(person)

person_json = json.dumps(person, indent=4) 
# indent could be 2,4,8. It beautifies the JSON
print(type(person_json))
print(person_json)

# # Saving as JSON File
# # We can save data as a JSON file. For writing a json file, use
# # the json.dump() method.
# person = {
#     "name": "valentino",
#     "country": "argentina",
#     "city": "corrientes",
#     "skills": [
#         "Python",
#         "Django"
#     ]
# }
# with open("./18_file_handling/json_example.json", "w", encoding="utf-8") as json_file:
#     json.dump(person, json_file, ensure_ascii=False, indent=4)