import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


from unittest import TestCase
from stock_ingester_tradier import StockIngester
from stock_displayer import StockDisplayer
class TestCovidDisplayer(TestCase):
    def test_display_days(self):
        stock_ing = StockIngester()
        result_dict = stock_ing.get_last_days()
        stock_dsp = StockDisplayer()
        stock_dsp.display_days(result_dict)
        plt.show()