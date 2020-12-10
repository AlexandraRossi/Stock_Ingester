import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np

from stock_ingester_tradier import StockIngester as si

class StockDisplayer:
    def display_days(self, ticker, data_dict):
        names = list(data_dict.keys())
        values = list(data_dict.values())
        #  {"2020-11-01": 234.5, "2020-11-02": 256.2,...}
        figure, axes = plt.subplots()
        axes.plot(names, values, label=ticker)
        axes.set(title="Stock")
        axes.tick_params(axis="x", labelrotation=90)
        axes.legend()
        plt.show()