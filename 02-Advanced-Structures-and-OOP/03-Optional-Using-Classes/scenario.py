# pylint: disable=missing-docstring

from portfolio import Portfolio

portfolio = Portfolio("Boris")
portfolio.buy( "AAPL", 10,  100)
portfolio.buy( "GOOG",  1, 1000)
portfolio.sell("AAPL",  5,  110)
portfolio.buy( "AAPL",  5,   90)
# portfolio.buy( "ZZZZ",  5,   90) # ZZZZ can't be find in `spot_prices`

spot_prices = {
    "AAPL": 120,
    "GOOG": 1100
}
pnl = portfolio.pnl(spot_prices)
print(f"P&L for {portfolio.trader_name}: {pnl}")
