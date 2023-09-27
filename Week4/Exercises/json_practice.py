import json



a = {"name": "John",
     "age":31,
     "Salary":25000}

b = json.dumps(a)
with open("Sample.json", "w") as p:
    json.dump(a, p, indent=2)