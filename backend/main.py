import uvicorn
from fastapi import FastAPI
from product import mongo_products
from order import mongo_orders

app = FastAPI()


@app.get("/products")
def read_products():
    return {"message": mongo_products}


@app.get("/orders")
def read_orders():
    return {"message": mongo_orders}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
