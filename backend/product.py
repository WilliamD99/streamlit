from mongodb import col_orders, col_products

mongo_products = list(col_products.find({}, {"_id": 0, "id": 1, "name": 1}))

for product in mongo_products:
    product_id = product["id"]
    product["total_sales"] = 0
    product["total_quantity"] = 0

    mongo_orders = list(col_orders.find(
        {
            "line_items.0.product_id": product_id  # Filter orders by product id
        },
        {
            "_id": 0,
            "id": 1,
            "line_items.total": 1,
            "line_items.quantity": 1
        }
        ))

    for order in mongo_orders:
        product["total_sales"] += float(order["line_items"][0]["total"])  # Calculate sales for each product
        product["total_quantity"] += float(order["line_items"][0]["quantity"])  # Calculate quantity bought for each product
    product["total_orders"] = len(mongo_orders) # Total order
    product["orders"] = mongo_orders


