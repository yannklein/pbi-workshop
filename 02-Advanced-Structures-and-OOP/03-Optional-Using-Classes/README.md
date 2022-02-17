# (Optional) Using Classes

For this third exercise, we will elaborate a bit on our portfolio example and consider a real-life situation of a trader. At the end of the day, a trader will have produced a series of deals:

| Stock | Way  | Volume | Strike |
|-------|------|--------|--------|
| AAPL  | BUY  | 10     | 154.12 |
| GOOG  | BUY  | 2      | 812.56 |
| AAPL  | SELL | 3      | 155.0  |
| ...   | ...  | ...    | ...    |


We are going to use Object Oriented Programming to properly manipulate this tabular information and compute a portfolio P&L based on spot prices of stocks.

## Methodology

This exercise uses TDD. Please make sure to run the unit tests in the folder `03-Using-Classes`:

![](https://res.cloudinary.com/wagon/image/upload/v1583774692/using_classes_all_red_bzbhyl.jpg)

They should all fail, as you haven't started coding yet, that's perfectly normal!

## The `Deal` class

Let's start with the simplest class of the exercise: `Deal`. This class will model a row in the table shown above :point_up:

Remember, when doing Object Oriented Programming and considering creating a new class, we have to figure out two things:

- The data (stored in instance variables)
- The behavior (implemented by instance methods)

This way, when we create instances of that class, each instance will hold specific data, and will be able to do some behavior when called.

### Instance Variables

Let's start with the data. What information should we store in the `Deal` class? Well, pretty much the columns in the table! Go ahead, open the `deal.py` file and code the `__init__` method of the `Deal` class, which will take 5 parameters:

- `self` (Python convention, it's mandatory)
- `symbol`, a string (e.g. `AAPL`)
- `volume`, a number (integer for stocks, float for commodities)
- `price`, a float
- `way`, a string, either `"BUY"` or `"SELL"`

When you are done, run the tests again. You should make **one test pass** (the `can_init_a_deal` one). Don't go on until this one pass!

### Instance Method

We will now implement some behavior on the `Deal` class. The goal is to build a small feature that we will use for the big P&L computation. We want to implement an instance method which takes a spot price and return the mark to market of that deal:

```python
# deal.py
# [...]

class Deal:
    # [...]

    def mtm(self, spot_price):
        # TODO: implement this method!
```

First example: we have a deal of 10 stocks of `AAPL` bought at $100. The spot price is $105, then the computed mtm is `($105 - $100) * 10 = $50`.

Second example: we have a deal of 20 stocks of `GOOG` sold at $200. The spot price is $210, then the computed mtm is `($200 - $210) * 20 = -$200`

Go ahead and implement that `mtm` instance method. Run the tests, you should have 4 more green tests (The ones starting with `test_mtm_`)!

## The `Portfolio` class

Now that we have a well-defined `Deal` class, it's time to consider the fact that a trader does _many_ deals every day. Those deals will be added to the portfolio, the goal being that we want to compute the total P&L of those deals.

Like for the `Deal` class, let's think about the two important things about Object Oriented Programming:

- The data (stored in instance variables)
- The behavior (implemented by instance methods)

Repetition is the first principle of all learning :wink:

### Instance Variables

We want our `Porfolio` to hold two pieces of information:

- The portfolio trader's name (a string)
- The `list` of deals in that portfolio

When starting a portfolio, the list of deals is **empty**, meaning that we should be able to instantiate a new one simply like this:

```python
boris_portfolio = Porfolio("Boris")
```

Go ahead and implement the `__init__` method of the `Portfolio` class. Run the tests: you should make the `test_init_portfolio` pass. Don't go on until it is green.

### Instance Methods

The behavior of the `Portfolio` is more diverse than the `Deal` class. We want to

- Store a `BUY` deal
- Store a `SELL` deal
- Compute the P&L of the portfolio

Implement the two first instance methods in the `portfolio.py` file of the folder `03-Using-Classes`:

```python
# portfolio.py

# [...]
class Portfolio:
    # [...]
    def buy(self, symbol, volume, price):
        # TODO:
        #    1. Create a BUY Deal instance
        #    2. Append it to the deals list

    def sell(self, symbol, volume, price):
        # TODO:
        #    1. Create a SELL Deal instance
        #    2. Append it to the deals list
```

Run the tests. The two tests starting with `test_can_store_*` should turn green. Don't go on until this is the case.

## P&L Computation

:pause_button: Let's pause the TDD approach for a few minutes.

We are still working in the `Portfolio` class, where we need to implement the `pnl` instance method. This method will take a dictionary of spot prices (keys: symbols, values: spot prices) to be used like this:

```python
portfolio = Portfolio("Boris")
portfolio.buy( "AAPL", 10,  100)
portfolio.buy( "GOOG",  1, 1000)
portfolio.sell("AAPL",  5,  110)
portfolio.buy( "AAPL",  5,   90)

spot_prices = {
    "AAPL": 120,
    "GOOG": 1100
}
pnl = portfolio.pnl(spot_prices)
print(f"P&L for {portfolio.trader_name}: {pnl}")
```

This scenario is already implemented in the `scenario.py` file. Open and **run** it in Spyder. You should get the following error in the IPython console:

```
AttributeError: 'Portfolio' object has no attribute 'pnl'
```

That's normal, you now need to define and implement that method in the `Portfolio` class (in the `portfolio.py` file). This is the most complicated method of this exercise, try first to compute with a pencil & paper based on the four deals of `AAPL` and `GOOG` listed in the scenario and the spot prices defined just after. Once you have a number, thing about the pseudo-code and write it down. When you are ready, you finally can do it in Python, but not before! This is the typical workflow of a programmer, and it takes practise!

Don't hesitate to `print()`, and run the code as often as possible. The IPython console is your friend here.

### TDD

Once you are confident about your implementation, go back to the `Unit testing` tab and run them. They should all pass **except** the `test_pnl_raises_error_if_missing_spot_price`. First of all, congratulations 💪 🚀 👏

The last test is here to make sure you think about potential **missing data**. Imagine the following scenario where you add **one** deal of the `ZZZZ` stock:

```python
portfolio.buy( "AAPL", 10,  100)
portfolio.buy( "GOOG",  1, 1000)
portfolio.sell("AAPL",  5,  110)
portfolio.buy( "AAPL",  5,   90)
portfolio.buy( "ZZZZ",  5,   90) # ZZZZ can't be find in `spot_prices`

spot_prices = {
    "AAPL": 120,
    "GOOG": 1100
}
pnl = portfolio.pnl(spot_prices)
```

We want our code to detect that `ZZZZ` has at least a deal but has **no spot price**. In that case, we want the code to [`raise`](https://docs.python.org/3/tutorial/errors.html) a `Warning`:

```python
raise Warning("A meaningful message for the user running the program!")
```

This last touch should make the 12th test of this exercise pass. Congratulations!

:bulb: Don't forget to **push your code to GitHub**
