import json

with open("products.json") as f:
    data = json.load(f)

    filtered_list = [product for product in data if product["price"] > 10 and product["price"] <50]

    filtered_list.sort(key=lambda x: x["name"])
    print(filtered_list)

