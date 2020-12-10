import http.client
import json
import ssl
from typing import Dict
import datetime as dt
import requests

Endpoint = 'https://sandbox.tradier.com/v1/markets/history'

API_KEY = "HczRZFiWaAr7dPsQJuXope7VtdYc3IMM"


class StockIngester:

    def get_last_days(self, ticker, start_date, end_date) -> Dict[str, int]:


            response = requests.get(Endpoint,
                                    params={'symbol': 'AAPL', 'interval': 'daily', 'start': '2020-11-05',
                                            'end': '2020-11-12'},
                                    headers={'Authorization': 'Bearer kiIYju5gyBzXJX7ScRKoqGhbCnS1',
                                             'Accept': 'application/json'})



            stock_dict = response.json()

            days_data_list = stock_dict["history"]['day']
            result_dict = {item["date"]: item["close"] for item in days_data_list}


            return result_dict