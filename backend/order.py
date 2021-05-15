from mongodb import col_orders

mongo_orders = list(col_orders.find(
    {},
    {
        "_id": 0,
        "id": 1,
        "date_created": 1,
        "status": 1,
        "billing.first_name": 1,
        "billing.last_name": 1,
        "line_items.name": 1,
        "line_items.quantity": 1,
        "line_items.subtotal": 1
     }))
