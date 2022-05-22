import pytest
import datetime
from fastapi.testclient import TestClient
from api_yahoo import get_info_data 
from main import app


client = TestClient(app)


def test_df_not_empty():   ### Checking if Pulled the data from Yahoo Finance
    stock = "AAPL"
    start_d  = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    end_d = datetime.date.today().strftime('%Y-%m-%d')
    interval_t = "1d"

    result = get_info_data(stock, start_d, end_d, interval_t)
    assert len(result) > 0  


def test_connect_server():    ### Checking that the connection was made correctly
    response = client.post("/db-alerts-stocks")
    assert response.status_code == 200


