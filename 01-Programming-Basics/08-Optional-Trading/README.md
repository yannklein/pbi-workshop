# Trading

For this exercise, we will use TDD. Some tests have already been written, you goal will be to make them pass.

In Spyder, Go to the `01-Programming-Basics/08-Optional-Trading` folder and open `financials.py`. This is where you will need to write the code.

Make sure you open `test_financials.py` too to be able to test your code.

## Forward Price

We want you to define a function, `forward_price` which takes three parameters:

- `spot` (float),
- `interest_rate` (float),
- `time` (float)

This function should compute and return the forward price, **rounded at 2 decimals**, of an asset in a forward contract using this formula:

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/forward_pricing_e7n4fh.png)

where:

- `F` is the forward price to be paid at time `T` (expressed in **years**)
- `r` is the [risk-free interest rate](https://en.wikipedia.org/wiki/Risk-free_interest_rate)
- `q` is the cost of carry
- `S0` is the spot price of the asset (at `t == 0`)
- `Di` is the dividend to be paid

Source: [Wikipedia](https://en.wikipedia.org/wiki/Forward_price)

:warning: To simplify the exercise, we'll assume that the cost of carry is **0** and the asset we are pricing **don't yield any dividend**, which greatly simplifies the formula.

The goal of this exercise is to write the function and make sure the tests related to the `forward_price` pass! Before running the tests, define an `short_pnl` function with just `pass` in its body (the second part of the exercice will be all about this function). Otherwise, the test file will try to import such a function, which will raise an error.

<details><summary markdown='span'> :bulb: Hint 1
</summary>

Don't forget to turn to Google as often as possible! Programming questions almost always have an answer in the Top 3 Search results. [Do it!](http://lmgtfy.com/?q=python+power)

</details>

<details><summary markdown='span'> :bulb: Hint 2
</summary>

In math, [`e`](https://en.wikipedia.org/wiki/E_(mathematical_constant)) is approximately `2.7182`. You can also use the `e` constant imported from the `math` module (exactly like what you did with π)!

You can also choose to use the [`math.exp()`](https://docs.python.org/2/library/math.html#math.exp) function from the `math` module. Your call!

</details>


## Profit & Loss Computation

Let's assume that we have a portfolio of positions on which we want to compute a P&L based on the [Mark to Market](https://www.investopedia.com/terms/m/marktomarket.asp) methodologies used in futures account to ensure that margin requirements are being met.

At the end of the trading day, we look at the market and get a **fair value** for each asset we have in the porftolio. The goal here is not to compute this fair value, we will get this information as an **input**.

To simplify, we will not consider any effect of the risk-free interest rate, and assume its value is `0`. We will also assume that we only have _one_ lot for each contract in the porfolio, meaning that the price of that contract at the end of the day is equal to the market price of the asset. We will also assume that we only hold **SHORT** positions (we are the seller in the contract position). This means that we will make a profit only if the strike price (at `t == 0`) is above the spot price at maturity (`t == T`).

We want you to define a function, `short_pnl` which takes two parameters:

- `positions` (list) of strike prices for each future contract
- `mtm` (list) of the current market value of each asset

To simplify the exercise, we will assume that `positions` and `mtm` lists have the **same length** and that the order is identical (first element in `positions` can be compared to the first element in `mtm`, etc.). We will also assume that all the futures in the portfolio are not yet up to maturity.

This function should compute and return the [P&L](https://en.wikipedia.org/wiki/Income_statement) (net income) of the portfolio.

Example:

I hold a porfolio of 3 future contracts on 3 different underlying assets:

- Future A (SHORT) with a strike price of 100
- Future B (SHORT) with a strike price of 140
- Future C (SHORT) with a strike price of 200

Tonight, the market closes and the following market prices are spotted:

- A closes at 110
- B closes at 120
- C closes at 180

The P&L portfolio can be computed like this:

```
(100 - 110) + (140 - 120) + (200 - 180) = 30
```

Before you jump into the code, please read [this about Python lists](https://www.programiz.com/python-programming/list). We will cover the subject extensively in tomorrow's lecture, but in the meantime you can start reading about it.

Your turn!


<details><summary markdown='span'> :bulb: Hint
</summary>

To loop over an array, you can use the following code:

```python
for element in array:
    print(element)
```

If you need to access the index of a list in a for loop, you can use the [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) function:

```python
for index, value in enumerate(a_list):
    print(index, value)

# e.g. if a_list = [ 7, 4, 19 ], it will print:
#   - 0, 7
#   - 1, 4
#   - 2, 19
```

</details>

## Pushing your code to GitHub

Don't forget to use GitHub Desktop to push your progress!
