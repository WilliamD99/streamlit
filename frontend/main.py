import requests
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

option = st.selectbox(
   'Analytics',
   ("Product", 'Order'))

if option == "Product":
    res = requests.get(f"http://localhost:8080/products")
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

    col1_header, col2_header, col3_header = st.beta_columns([1, 1, 1])

    with col1_header:
        st.header("Items Sold")
        st.subheader(sum(categorized_order["Items Sold"]))
    with col2_header:
        st.header("Net Sales")
        st.subheader(sum(categorized_order["Net Sales"]))
    with col3_header:
        st.header("Orders")
        st.subheader(sum(categorized_order["Orders"]))

    col1, col2 = st.beta_columns([1, 1])
    col1.bar_chart(product_sales_pd)
    col2.bar_chart(product_to_pd)

    st.table(product_overview_pd)
else:
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

    col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 1])
    number_of_orders = len(total_orders["Date"])
    total_sales = sum(total_orders["Net Sales"])
    total_product_sales = sum(total_orders["Items Sold"])

    with col1:
        st.header("Orders")
        st.subheader(number_of_orders)
    with col2:
        st.header("Net Sales")
        st.subheader("${}".format(total_sales))
    with col3:
        st.header("Average Order Value")
        st.subheader("${}".format(f'{total_sales / number_of_orders: .2f}'))
    with col4:
        st.header("Average Items Per Order")
        st.subheader(round(total_product_sales / number_of_orders))

    st.table(total_orders_pd)





