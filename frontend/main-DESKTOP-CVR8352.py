import requests
import streamlit as st
import pandas as pd

res = requests.get(f"http://localhost:8080/orders")
categorized_order = res.json()["message"]

# Product Order
product_order = {"Product": [], "Total order": []}
for key in categorized_order.keys():
    product_order["Product"].append(categorized_order[key][1])
    product_order["Total order"].append(categorized_order[key][0])
product_order_pd = pd.DataFrame(data=product_order["Total order"], index=product_order["Product"])

st.title("Categorized by Products")
st.write(product_order_pd)
st.bar_chart(product_order_pd, height=500)

# Product Sales
product_sales = {"Product": [], "Sales": []}
for key in categorized_order.keys():
    i = 2 # First 2 eles in the list are not orders
    product_total = 0
    while i < len(categorized_order[key]):
        product_total += float(categorized_order[key][i]["total"])
        i += 1
    product_sales["Sales"].append(product_total)
    product_sales["Product"].append(categorized_order[key][1])

product_sales_pd = pd.DataFrame(data=product_sales["Sales"], index=product_sales["Product"])
st.bar_chart(product_sales_pd, height=500)

plot = product_sales_pd.plot(y=product_sales["Sales"])
st.write(plot)



