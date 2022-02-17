# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/2/15 3:22 PM
# @Author    :ChenCheng

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def index():
    return {"hello": "world"}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def search_item(page: int = 0, query: str = ''):
    return {"page": page, "query": query}


@app.post("/items/")
async def create_items(item: Item):
    return item


if __name__ == '__main__':
    pass