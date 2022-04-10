from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, NoneBytes


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}

@app.get('/items/{item_id}')
def get_item(item_id: int, q: Optional[str]=None):
    return {'item_id': item_id, 'q': q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item_name': item.name}