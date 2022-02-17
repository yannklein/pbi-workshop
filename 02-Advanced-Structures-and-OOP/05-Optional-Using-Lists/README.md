# Using lists

[List](https://docs.python.org/3/tutorial/introduction.html#lists) is a fundamental compound data type that you will find in almost every programming language (in other languages, we call it _Array_). A Python list holds elements (of any type) in memory. We can perform CRUD operations on it meaning that we can read a stored element, add an element, update an element and delete an element.

Lists are **indexed** by integers, with the first element being indexed at `0`. You can think of how it's stored in memory with the following diagram:

```python
words = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
```

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/list_ttgeba.png)

Lists have some great properties:

- They are **ordered** thanks to their indexes
- They can contain any number of arbitrary objects (integer, float, string or even list and dictionaries as well!)
- List elements can be accessed by their index
- Lists are mutable & dynamic (you can change them and add any number of elements you want without worrying about memory management)

## Exercise - Nested array

We are going to model a portfolio of stocks on the [NASDAQ](https://www.nasdaq.com/) market. Let's say we hold the following positions:

- [`AAPL`](https://www.nasdaq.com/symbol/aapl): 10 stocks bought at $154.12
- [`GOOG`](https://www.nasdaq.com/symbol/goog):  2 stocks bought at $812.56
- [`TSLA`](https://www.nasdaq.com/symbol/tsla): 12 stocks bought at $342.12
- [`FB`](https://www.nasdaq.com/symbol/fb): 18 stocks $209

For each stock we need to store **two** pieces of information:

- The volume
- The strike price (price at which we bought the option)

We simplify and suppose we bought all the stocks at the same point in time (one strike price / stock). We can use a list to store both information:

```python
aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]
```

This approach will create many variables with a big portfolio. We'd like to regroup this information into just one list. We can do it like so:

```python
portfolio = [ aapl, goog, tsla, fb ]
```

You can see that we have created a **nested** array. `portfolio` is a variable containing a list, and each element of that list is a list too!

:question: From `portfolio`, how can you access the number of Facebook stocks in that portfolio? Try it in Spyder by first running the `portfolio.py` file and then test it in your IPython console.

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/portfolio_ipython_x84rvl.png)

Compare your approach with your buddy's before looking at the solution

<details><summary markdown='span'>View solution
</summary>

Facebook is the 4th element in the Portfolio, so we can access it with the index `3` which will yield a list of two elements. First element is the number of stocks, second element is the strike price. To answer the question, we need to write the following code:

```python
fb_stocks_count = portfolio[3][0]
```

</details>

### P&L Computation

In order to compute the current P&L of our `portfolio`, we want to compare the strike price to the spot price of each asset (taking into account the volume). Let's suppose the market currently holds the following spot prices:

```python
#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]
```

Copy-paste this new variable in Spyder, and try to compute the `pnl` of your portfolio against the `market`. This exercise is not done with TDD, just run the code and `print()` what you need to debug. Talk with your buddy and reach out to a TA whenever you are blocked.

<details><summary markdown='span'> :bulb: Hint
</summary>
You should find that the portfolio is <strong>losing -$174.5</strong>, mainly because of Tesla's stock's bad performance!
</details>

### Some questions

Here are some open questions for you to think about, discuss them with your buddy and TAs:

- `portfolio` is a nested list, is it a good approach? Why?
- Is there a link between the order / number of elements in `portfolio` and `market`. Is it realistic? What's the problem?
- How would you improve this system to be more resilient, using only the type `list`?
- What type should we introduce to improve our code?

Once you have some answers about those questions, it's time to go to the next exercise.

## Pushing your code to GitHub

Remember the steps we did yesterday to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `portfolio.py` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Complete the first exercise using Lists`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window

That's it! Take a small break before diving into the `Using Dictionaries` exercise.
