from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Updated"}

@app.get("/items/{item_id}")
def read_item(item_id: int,q : str = None ):
    return {"item_id": item_id, "q" : q,}



@app.post("/items/")
def create_item(item : Item):
    return {"name": item.name, "price" : item.price, "is_offer" : item.is_offer}