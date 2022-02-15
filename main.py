# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/2/15 3:22 PM
# @Author    :ChenCheng

from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}