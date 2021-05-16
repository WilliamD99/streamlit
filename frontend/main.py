import streamlit as st
import pandas as pd
from options.product import categorized_order, product_sales_pd, product_to_pd, product_overview_pd
from options.order import total_orders_pd, number_of_orders, total_sales, total_product_sales

st.set_page_config(layout="wide")

option = st.selectbox(
   'Analytics',
   ("Product", 'Order'))

if option == "Product":
    col1_header, col2_header, col3_header = st.beta_columns([1, 1, 1])
    with col1_header:
        st.header("Items Sold")
        st.subheader(sum(categorized_order["Items Sold"]))
    with col2_header:
        st.header("Net Sales")
        st.subheader("${}".format(sum(categorized_order["Net Sales"])))
    with col3_header:
        st.header("Orders")
        st.subheader(sum(categorized_order["Orders"]))

    col1_chart, col2_chart = st.beta_columns([1, 1])
    with col1_chart:
        st.subheader("Sales By Products")
        st.bar_chart(product_sales_pd)
    with col2_chart:
        st.subheader("Total Orders")
        st.bar_chart(product_to_pd)

    st.table(product_overview_pd)
else:
    col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 1])
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





