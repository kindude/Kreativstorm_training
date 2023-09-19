
try:
    with open("uppercase.txt", "r") as file:
        content = file.read()
        print(content)
        upper_content = content.upper()
        print(upper_content)
except FileNotFoundError as error:
    print(f"File not found {error}")