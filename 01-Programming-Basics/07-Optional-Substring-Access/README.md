# Middle String
In this exercise we'll give you three strings and ask you to find and return the second biggest (in size).

The goal of this exercise is to practice one of the most important and fundamental way to work when you code : divide by use. The idea behind is that it is much easier to tackle smaller problems and that if some code can be reused then it is best practice to encapsulate it in a function to not have to rewrite the code later but just call that function.
This means that we're going to divide our exercise in 3 steps to be able to accomplish our goal.

Open `find_middle_string.py` and solve this exercise by using functions with defined responsibilities.
Each one is specified with what we call a *docstring* delimited by 3 `'"'`. As usual tests are available to check your code.

## Advices
For this exercise remember that `print` and `return` do not have the same impact in a function.

```python
def example():
    a = 1
```

In the example written above, if we want to print what the `a` variable contains in the terminal, we'll use:

```python
def example():
    a = 1
    print(a)
```

If we want that our function call gives the value of a, we'll use:

```python
def example():
    a = 1
    return a
```

## First step : len
The first step is to create a function that will return the size of a string. Usually in python you can (should and will!) use the `len()` built-in function to get the size of a string (or a list), but for today's exercise we'll ask you to implement your own function that calculates the size of a string.

You'll implement the body of `get_size_of_string`, remember it has to return an int : the size of the string.

<details><summary markdown="span">Hint
</summary>
Use a for loop on the string.
</details>

<details><summary markdown="span">View solution
</summary>

```python
def get_size_of_string(string):
    count = 0
    for i in string:
        count += 1
    return count
```
</details>

## Second step : middle value
The second step is to create a function that will return the middle value between three number (remember those have to be integer like our size!).
This function should return -1 if two values are equal.

```python
get_middle_value(2, 1, 3)
```
should return 2 and

```python
get_middle_value(1, 2, 2)
```
should return -1
<details><summary markdown="span">Hint
</summary>
a could be bigger than b and smaller than c, but the opposite exists too.
</details>
<details><summary markdown="span">View solution
</summary>

```python
def get_middle_value(a, b, c):
    if b > a > c or c > a > b:
        return a
    elif a > b > c or c > b > a:
        return b
    elif a > c > b or b > c > a:
        return c
    else:
        return -1
```
</details>

## Last step : find middle string
Our last step is to create a function that takes 3 strings as parameters and return the second biggest. To do so, you'll of course need to use the two functions that we just wrote.

```python
find_middle_string("hello", "allo", "bonjour")
```
Should return `"hello"`.

Note that if two of the provided strings have the same length, you should return `"two or more strings have the same length"`.


<details><summary markdown="span">Hint
</summary>
You'll have to check what number get_middle_value gives you back and return the appropriate string.
</details>
<details><summary markdown="span">View solution
</summary>

```python
def find_middle_string(string1, string2, string3):
    len1 = get_size_of_string(string1)
    len2 = get_size_of_string(string2)
    len3 = get_size_of_string(string3)
    middle_value = get_middle_value(len1, len2, len3)
    if middle_value == len1:
        return string1
    elif middle_value == len2:
        return string2
    elif middle_value == len3:
        return string3
    else:
        return "two or more strings have the same length"
```
</details>

## Pushing your code to GitHub

Don't forget to use GitHub Desktop to push your progress!
