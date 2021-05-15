from backend.helper.config import wcapi
from ..mongodb import db

# Select collections
col_orders = db.get_collection("wc_orders")
col_products = db.get_collection("wc_products")

# Add wc orders to mongo
for page_num in range(1, 101):  # Woocommerce response in pages, each page has 10 orders (100 pages in total)
    orders = wcapi.get("orders?page={}".format(page_num)).json()
    col_orders.insert_many(orders)

# Add wc products to mongo
products = wcapi.get("products?per_page=20").json()
col_products.insert_many(products)
