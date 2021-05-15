from woocommerce import API
import os
from dotenv import load_dotenv

load_dotenv()
woo_url = os.getenv('WOO_URL')
woo_ck = os.getenv('WOO_CK')
woo_sc = os.getenv('WOO_CS')

wcapi = API(
    url=woo_url,
    consumer_key=woo_ck,
    consumer_secret=woo_sc,
    version="wc/v3"
)