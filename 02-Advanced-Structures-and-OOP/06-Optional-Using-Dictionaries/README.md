# Using dictionaries

The previous exercise has shown some limitations of lists, especially to store information which does not have an _intrisic order_. For this exercise, we will use a Python [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

## Modelling the portfolio

In the previous exercise we had the following code:

```python
#       vol  strike
aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
```

In Spyder, open the `portfolio_advanced.py` file, define a `portfolio` variable and assign to it a dictionary holding all the information (volume and strike price). Whenever you need to define a dictionary, there are always two questions to answer _beforehand_:

- What are the keys? What type?
- What are the values? What type?

<details><summary markdown='span'>View solution
</summary>

We are going to store the stock symbol as keys (`AAPL`, `GOOG`, etc.) and we can also decide to store a dictionary as value to hold volume and strike.

```python
# portfolio_advanced.py
portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "FB": {
    "volume": 18,
    "strike": 209.0
  }
}
```

</details>

Once your `portfolio` is ready, can you answer the following questions with Python code? You can use the IPython console like in the previous exercise:

- Print the volume of `TSLA` stocks in the portfolio
- Print the strike of `GOOG` in the portfolio

<details><summary markdown='span'>View solution
</summary>

```python
print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])
```

</details>


### P&L Computation

Let's now compute the P&L of the `portfolio`. Once again, we need to have information about the spot prices of the Market! In the previous exercise we used the following representation:

```python
market = [ 198.84, 1217.93, 267.66, 179.06 ]
```

This is very weak. How would you improve that, using a dictionary? Try and define your own `market` variable in the `portfolio_advanced.py` file.

<details><summary markdown='span'>View solution
</summary>

Once again, we can (and should!) use the stock symbol as keys:

```python
market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "FB":    179.06
}
```

</details>

You now can write a small algorithm using information from both `market` and `portfolio` to compute the P&L.

<details><summary markdown='span'> :bulb: Hints
</summary>

You should find the same loss as the previous exercise as we took the exact same numerical value!

If you don't remember how to use a `for` loop over a Dictionary, [read this article](https://dev-notes.eu/2017/09/iterating-over-dictionary-in-python/)

</details>

Compare the code you've just wrote with the one from the previous exercise. Which one do you prefer? Which one is more explicit? Don't hesitate to exchange opinions with your buddy and TAs.

### (Optional) API

Instead of defining a fixed and fictional list of spot prices for the four stocks in the `portfolio`, we can go on the Internet and fetch **real-time spot prices**. We will cover API later in the week, but we can already have a test for it.

We can use the **IEX** trading API. By reading the documentation, we can see there is an endpoint to retrieve the last price for a list of symbols: [`/tops/last?symbols=...`](https://iextrading.com/developer/docs/#last)

Go ahead and open the following URL in a new tab in your browser:

:point_right: [`https://cloud.iexapis.com/stable/tops/last?token=pk_1cd4889a6bbd49d8a8c3576f0c0e3fcf&symbols=AAPL,GOOG,TSLA,FB`](https://cloud.iexapis.com/stable/tops/last?token=pk_1cd4889a6bbd49d8a8c3576f0c0e3fcf&symbols=AAPL,GOOG,TSLA,FB)

Calling an API with Python is usually done thanks to the third-party module [`requests`](http://docs.python-requests.org/en/master/). In your IPython console, try the following code:

```python
import requests

url = "https://cloud.iexapis.com/stable/tops/last?token=pk_1cd4889a6bbd49d8a8c3576f0c0e3fcf&symbols=AAPL,GOOG,TSLA,FB"
real_time_market = requests.get(url).json()
```

What can you see? What is `type(real_time_market)`? is it close to the structure of our `market` variable? How could we make it closer so that we could swap the hard-coded data?

Try to play a bit with the data in the IPython console, talk with your buddy and ask TAs.

<details><summary markdown='span'>View solution
</summary>

The idea is to iterate over the `real_time_market` list and extract information to build the `market` dictionary:

```python
market = {}

for stock in real_time_market:
    market[stock['symbol']] = stock['price']
```

These 3 lines of code can actually be replaced by a **list comprehension**:

```python
market = dict((stock['symbol'], stock['price']) for stock in real_time_market)
```

</details>

Last question: if you look at the URL of the API call, you can see that the four symbols are **hard-coded**. What if I buy 10 `AMZN` stocks at $1812.11?

```python
portfolio["AMZN"] = {
  "volume": 10,
  "strike": 1812.11
}
```

:question: How can you change the API call so that the list of symbols is **dynamically** computed based on the `portfolio` content?

<details><summary markdown='span'> :bulb: Hint
</summary>

You need to use the [`.keys()`](https://www.tutorialspoint.com/python/dictionary_keys.htm) method on a Dictionary and the [`.join()`](https://www.tutorialspoint.com/python/string_join.htm) on a string

</details>

<details><summary markdown='span'>View solution
</summary>

You need to update your code with the following:

```python
symbols = ",".join(portfolio.keys())
url = f"https://api.iextrading.com/1.0/tops/last?token=pk_1cd4889a6bbd49d8a8c3576f0c0e3fcf&symbols={symbols}"
real_time_market = requests.get(url).json()
```

</details>

---

Congratulations on finishing this exercise! You should have a better understanding of the inner workings of `list` and `dict`. Time to see how we can introduce Classes with the next exercise.

:bulb: Don't forget to **push your code to GitHub**
