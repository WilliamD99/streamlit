import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('USER_NAME')
pw = os.getenv('PW')
cluster = os.getenv('CLUSTER')

connect_str = "mongodb+srv://{}:{}{}}".format(username, pw, cluster)
client = pymongo.MongoClient(connect_str)
db = client["myFirstDatabase"]

col_orders = db.get_collection("wc_orders")
col_products = db.get_collection("wc_products")