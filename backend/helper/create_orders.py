from woocommerce import API
from faker import Faker
import random
from config import wcapi
woo_ck = "ck_a55d848acaad86dbfee3f457be52f65826671d42"
woo_sc = "cs_ae368ac524afc150fb656185128056abed57f4a2"
woo_url = "https://woocommerce-586409-1898674.cloudwaysapps.com/"

fake = Faker()

# wcapi = API(
#     url=woo_url,
#     consumer_key=woo_ck,
#     consumer_secret=woo_sc,
#     version="wc/v3"
# )

def create_order():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    product_id = random.randint(20, 43)
    product_quantity = random.randint(1,10)

    wcapi.post("orders", {
    "payment_method": "cod",
    "payment_method_title": "Cash On Delivery",
    "set_paid": "True",
    "billing": {
        "first_name": first_name,
        "last_name": last_name,
        "address_1": "969 Market0",
        "address_2": "",
        "city": "Vancouver",
        "state": "BC",
        "postcode": "V5S3P3",
        "country": "CA",
        "email": email,
        "phone": "(555) 555-5555"
    },
    "shipping": {
        "first_name": first_name,
        "last_name": last_name,
        "address_1": "969 Market",
        "address_2": "",
        "city": "Vancouver",
        "state": "BC",
        "postcode": "V5S3P3",
        "country": "CA"
    },
    "line_items": [
        {
            "product_id": product_id,
            "quantity": product_quantity
        }
    ],
    "shipping_lines": [
        {
            "method_id": "flat_rate",
            "method_title": "Flat Rate",
            "total": "10.00"
        }
    ]
})

for i in range(1000):
    create_order()