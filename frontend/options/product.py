import requests
import pandas as pd

res = requests.get(f"http://host.docker.internal:8080/products")
data = res.json()["message"]

categorized_order = {"Product": [], "SKU": [], "Net Sales": [], "Items Sold": [], "Orders": [], "Category": []}

for order in data:
    categorized_order["Product"].append(order["name"])
    categorized_order["SKU"].append(order["sku"])
    categorized_order["Net Sales"].append(order["total_sales"])
    categorized_order["Items Sold"].append(order["total_quantity"])
    categorized_order["Orders"].append(len(order["orders"]))
    categorized_order["Category"].append(order["categories"][0]["name"])

product_sales_pd = pd.DataFrame(data=categorized_order["Net Sales"], index=categorized_order["Product"])
product_to_pd = pd.DataFrame(data=categorized_order["Items Sold"], index=categorized_order["Product"])
product_overview_pd = pd.DataFrame(data=categorized_order)
