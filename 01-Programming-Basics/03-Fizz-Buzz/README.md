# Fizz Buzz

The goal of this exercise is to implement a [Fizz Buzz](https://en.wikipedia.org/wiki/Fizz_buzz), which is a group word game for children to teach them about euclidean division and remainders.

In Wikipedia's words:

> Players generally sit in a circle. The player designated to go first says the number "1", and each player thenceforth counts one number in turn. However, any number **divisible by three** is replaced by the word **fizz** and any **divisible by five** by the word **buzz**. Numbers **divisible by both** become **fizzbuzz**. A player who hesitates or makes a mistake is eliminated from the game.

For example, a typical round of the game would be:

- 1
- 2
- fizz
- 4
- buzz
- fizz
- 7
- 8
- fizz
- buzz
- 11
- fizz
- 13
- 14
- fizzbuzz
- 16
- etc.

This exercise is now famous since 2007 as [Jeff Atwood](https://blog.codinghorror.com/about-me/), creator of StackOverflow and Discourse, wrote a blog post called [_Why Can't Programmers.. Program?_](https://blog.codinghorror.com/why-cant-programmers-program/). Really interesting!

N.B.: To simplify, we will assume that the game **stops when reaching the number `100`**.

## First steps

Like in the previous exercise, we will start to implement this game in the `fizz_buzz.py` empty file, without unit tests.

Before jumping right into the Python code, try to write **pseudo-code** with **comments** (lines that start with `#`). Try to write in **plain English** what you want the computer to do. Remember, the computer is very dumb, you need to be precise and thorough!

Once you think you are done with the pseudo-code, talk about it with your buddy, validate with a TA. Alternatively, you can have a look at the pseudo-code below:

<details><summary markdown='span'>View pseudo-code
</summary>

We need a **loop**! Should we use a `while` or a `for` loop? As we _know in advance how many iterations we need_ (100), then it's easier to use a `for`. We also need to use an `if` condition, coupled with some `else`. Here's the algorithm in plain English:

```python
# For n from 1 to 100
#     if n is divisible by 3
#         print 'fizz'
#     else if n is divisble by 5
#         print 'buzz'
#     else if n is divisible by 3 and by 5
#         print 'fizzbuzz'
#     else
#         print n
```

:warning: Beware, this pseudo-code contains a **bug** :bug: - Can you spot it? If you don't, carry on, it will reveal itself later...

</details>

## Implementation

Now that we've written the pseudo-code, time to actually implement it with Python! Here's a starter code to help you with the tricky part: counting from 1 to 100:

```python
for n in range(1, 100 + 1):
    print(n)
```

You can copy-paste the code above write it in the `fizz_buzz.py` file, below your pseudo code. Try to run it, can you see all the numbers from `1` to `100`? Good, you have the baseline! Now try to translate the pseudo-code into Python. Talk with your buddy, and ask a TA if you are stuck.

## The bug

Did you spot the bug? What about the number `15`? How can you fix it?

## (Optional) Refactoring

Try to extract your code in to a `fizz_buzz(max)` function which take one integer parameter, so that `100` is not hard coded anymore. Once done, you should be able to call your code like this:

```python
print("---")
print("Counting Fizz Buzz up to 5...")
fizz_buzz(5)

print("---")
print("Counting Fizz Buzz up to 30...")
fizz_buzz(30)
```

## Pushing your code to GitHub

Again, let's save our progress with GitHub Desktop. Try to repeat what you did for the first two exercises. If you have a doubt, look at the instructions from the `Playground` exercise, and if it is still unclear, don't hesitate to ask a TA.

## What's next?

For some exercises you will have the possibility to choose between a standard exercise and an exercise with Data more oriented on a trade. 
Take the one you like the most, the 2 exercises are similar on the concepts used. The choice is mainly based on your focus and expectations, you may prefer to proceed with different subjects for the exercises when there is an alternative. 
