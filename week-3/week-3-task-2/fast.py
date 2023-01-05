from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI()


# define a model for the data
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# create an in-memory database
items = {
    "item1": {"name": "item1", "price": 25.99, "is_offer": True},
    "item2": {"name": "item2", "price": 10.99, "is_offer": False},
}


# create a GET endpoint to retrieve items
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return items[item_id]


# create a POST endpoint to add new items
@app.post("/items/")
async def create_item(item: Item):
    item_id = str(uuid4())
    items[item_id] = item.dict()
    if not items:
        return "Some data is missing"
    else:    
         return {"id": item_id, **item.dict()}
    

# create a PUT endpoint to update existing items
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    if item_id in items:
        items[item_id] = item.dict()
        return {"id": item_id, **item.dict()}
    return {"error": "item not found"}


# create a DELETE endpoint to delete items
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if item_id in items:
        del items[item_id]
        return {"status": "success"}
    return {"error": "item not found"}






