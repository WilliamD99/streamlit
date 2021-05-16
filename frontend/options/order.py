import requests
import pandas as pd

res = requests.get(f"http://localhost:8080/orders")
data = res.json()["message"]

total_orders = {"Date": [], "Order#": [], "Status": [], "Customer": [], "Product(s)": [], "Items Sold": [], "Net Sales": []}

for order in data:
    date = order["date_created"].split("T")[0]
    name = order["billing"]["first_name"] + " " + order["billing"]["last_name"]

    total_orders["Date"].append(date)
    total_orders["Order#"].append(order["id"])
    total_orders["Status"].append(order["status"])
    total_orders["Customer"].append(name)
    total_orders["Product(s)"].append(order["line_items"][0]["name"])
    total_orders["Items Sold"].append(order["line_items"][0]["quantity"])
    total_orders["Net Sales"].append(float(order["line_items"][0]["subtotal"]))

total_orders_pd = pd.DataFrame(total_orders)
number_of_orders = len(total_orders["Date"])
total_sales = sum(total_orders["Net Sales"])
total_product_sales = sum(total_orders["Items Sold"])