import unittest
from pprint import pprint

import stock_ingester_tradier as si


class MyTestCase(unittest.TestCase):
    def test_get_last_days(self,):
        ingester = si.StockIngester()
        results = ingester.get_last_days("AAPL", "2020-11-31", "2020-12-05")
        pprint(results)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()