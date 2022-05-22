from doctest import FAIL_FAST
import json


def local_db():    ### Local db
    filename = 'data.json'
    with open(filename, "r") as file:
        db_stocks = json.load(file)
    return db_stocks