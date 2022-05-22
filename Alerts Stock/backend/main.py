import json
from typing import List
from db import local_db
from patterns import *
import pandas as pd
import datetime
from api_yahoo import get_info_data
from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
import uvicorn


class basic_info(BaseModel):
    stock_name: str
    up_trends: bool
    start_d = (datetime.date.today() -
               datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    end_d = datetime.date.today().strftime('%Y-%m-%d')
    interval_t = "1d"
    price_trigger: float


class stocks(BaseModel):
    stock_name: List[basic_info]


class stock_data(BaseModel):
    stock_name: str
    up_trends: bool
    price_trigger: float


stocks_list = stocks(stock_name=local_db())

app = FastAPI()


# Checking if trigger goes into action and send appropriate message
@app.get("/db-alerts-stocks")
async def get_alert():
    dic = {}
    for stock in stocks_list.stock_name:
        cur_price = get_info_data(
            stock.stock_name, stock.start_d, stock.end_d, stock.interval_t)

        if stock.up_trends:
            result = up_trend(cur_price, stock.price_trigger, stock.stock_name)
            if result:
                dic.update(
                    {stock.stock_name: f' in trigger and cut up {stock.price_trigger}$'})
            else:
                dic.update({stock.stock_name: ' is not in trigger'})
        else:
            result = down_trend(
                cur_price, stock.price_trigger, stock.stock_name)

            if result:
                dic.update(
                    {stock.stock_name: f' in trigger and cut down {stock.price_trigger}$'})
            else:
                dic.update({stock.stock_name: ' is not in trigger'})

    return (dic)


@app.get("/get_data")
async def get_data():
    data = json.load(open('data.json'))
    return (data)


@app.post("/add_data/")
async def get_data(item: stock_data):
    entry = {"stock_name": item.stock_name, "up_trends": item.up_trends, "price_trigger": item.price_trigger}
    filename = 'data.json'
    with open(filename, "r") as file:
        data = json.load(file)
    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file)
    return ("Data added succesfully!")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
