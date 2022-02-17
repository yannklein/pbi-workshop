# pylint: disable=missing-docstring

import inspect
import unittest

from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        if len(inspect.signature(Portfolio.__init__).parameters) > 2:
            self.portfolio = Portfolio("Boris", [])
        else:
            self.portfolio = Portfolio("Boris")

    def tearDown(self):
        self.portfolio = None

    def test_init_portfolio(self):
        self.assertEqual(self.portfolio.trader_name, "Boris")
        self.assertEqual(self.portfolio.deals, [])

    def test_can_store_a_buy_deal(self):
        self.portfolio.buy("AAPL", 10, 100)
        self.assertEqual(len(self.portfolio.deals), 1)
        deal = self.portfolio.deals[0]
        self.assertEqual(deal.symbol, "AAPL")
        self.assertEqual(deal.volume, 10)
        self.assertEqual(deal.price, 100)
        self.assertEqual(deal.way, "BUY")

    def test_can_store_a_sell_deal(self):
        self.portfolio.sell("AAPL", 10, 100)
        self.assertEqual(len(self.portfolio.deals), 1)
        deal = self.portfolio.deals[0]
        self.assertEqual(deal.symbol, "AAPL")
        self.assertEqual(deal.volume, 10)
        self.assertEqual(deal.price, 100)
        self.assertEqual(deal.way, "SELL")

    def test_pnl_one_buy(self):
        self.portfolio.buy("AAPL", 10, 100)
        spot_prices = { "AAPL": 200 }
        pnl = self.portfolio.pnl(spot_prices)
        self.assertEqual(pnl, 1000)

    def test_pnl_one_sell(self):
        self.portfolio.sell("AAPL", 10, 100)
        spot_prices = { "AAPL": 200 }
        pnl = self.portfolio.pnl(spot_prices)
        self.assertEqual(pnl, -1000)

    def test_pnl_complex_scenario(self):
        self.portfolio.buy( "AAPL", 10, 100)
        self.portfolio.buy( "GOOG", 1, 1000)
        self.portfolio.sell("AAPL",  5, 110)
        self.portfolio.buy( "AAPL", 5, 90)
        spot_prices = { "AAPL": 200, "GOOG": 2000 }
        pnl = self.portfolio.pnl(spot_prices)
        self.assertEqual(pnl, 2100)

    def test_pnl_raises_error_if_missing_spot_price(self):
        self.portfolio.buy( "TSLA", 10, 100)
        with self.assertRaises(Warning):
            spot_prices = { "AAPL": 200 }
            self.portfolio.pnl(spot_prices)

if __name__ == '__main__':
    unittest.main()
