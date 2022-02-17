# pylint: disable=missing-docstring

import unittest

from deal import Deal

class TestDeal(unittest.TestCase):
    def test_can_init_a_deal(self):
        deal = Deal("AAPL", 1, 100, 'BUY')
        self.assertEqual(deal.symbol, "AAPL")
        self.assertEqual(deal.volume, 1)
        self.assertEqual(deal.price, 100)

    def test_mtm_for_a_buy(self):
        deal = Deal("AAPL", 1, 100, 'BUY')
        self.assertEqual(deal.mtm(200), 100)

    def test_mtm_for_a_sell(self):
        deal = Deal("AAPL", 1, 100, 'SELL')
        self.assertEqual(deal.mtm(200), -100)

    def test_mtm_for_a_buy_with_multiple_volume(self):
        deal = Deal("AAPL", 10, 100, 'BUY')
        self.assertEqual(deal.mtm(200), 1000)

    def test_mtm_for_a_sell_with_multiple_volume(self):
        deal = Deal("AAPL", 10, 100, 'SELL')
        self.assertEqual(deal.mtm(200), -1000)

if __name__ == '__main__':
    unittest.main()
