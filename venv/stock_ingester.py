import http.client
import json
import ssl
from typing import Dict
import datetime as dt

API_KEY = "HczRZFiWaAr7dPsQJuXope7VtdYc3IMM"


class StockIngester:

    # Constructor
    def __init__(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.verify_mode = ssl.CERT_NONE
        self.conn = http.client.HTTPSConnection("api.polygon.io",
                                                context=self.context)

        # https://api.polygon.io/v1/open-close/AAPL/2020-10-14?apiKey=AwsfBb8lyNE89_VifeFWhs9caGO1PpfK


    # Destructor
    def __del__(self):
        self.conn.close()

    def get_last_five_days(self, ticker) -> dict[str, int]:
        today = dt.date.today()
        result_dict = {}
        ticker = "AAPL"

        for days_back in range(1, 6):
            past_date = today - dt.timedelta(days=days_back)

            self.conn.request("GET", f"/v1/open-close/{ticker}/{past_date}?apiKey={API_KEY}")
            res = self.conn.getresponse()
            data = res.read()
            json_string = data.decode("utf-8")
            stock_dict = json.loads(json_string)

            close_price = stock_dict["close"]

            result_dict[str(past_date)] = [close_price]

        return result_dict