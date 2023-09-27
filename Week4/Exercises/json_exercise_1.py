import json

company_data = '''
{
    "company_name": "Acme Corporation",
    "departments": [
        {
            "name": "HR",
            "employees": [
                {"name": "Alice", "salary": 60000},
                {"name": "Bob", "salary": 55000}
            ]
        },
        {
            "name": "Engineering",
            "employees": [
                {"name": "Charlie", "salary": 80000},
                {"name": "David", "salary": 75000}
            ]
        }
    ]
}'''


data = json.loads(company_data)

departments = data["departments"]

for department in departments:
    for employee in department["employees"]:
        if employee["name"] == "David":
            print(f"Name: {employee['name']}\nSalary: {employee['salary']}")
