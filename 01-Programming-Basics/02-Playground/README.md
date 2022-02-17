# Playground

Before we resume working on exercises using TDD, let's try to recap all the concepts seen in the lecture and manipulate them freely. The goal is to get used to the Spyder environment, the text editor zone, and the IPython console.

## Variable & Types

Can you explain to your buddy what is a type? What is a variable? Once you agree on those two concepts, let's write some code.

In Spyder, in the *File explorer*, go to the `01-Programming-Basics/02-Playground` folder in `python-beginners`. Double click on `playground.py` to open the empty file.

Let's compute information about a circle and a disk based on the radius.

- Define a `radius` variable and **assign** any positve number you want
- Define a `perimeter` variable and assign to it the right computation using the `radius` variable
- Print the value of the `perimeter` variable
- ![](https://res.cloudinary.com/wagon/image/upload/v1562058697/green_arrow_xr54uz.png) Run your code. Do you get the right result in the IPython console? If not, ask your buddy
- Define an `area` variable and assign to it the right computation.
- Print the value of the `area` variable

<details><summary markdown="span">Hint
</summary>

For π, you can use either `3.14` or a more precise value from the Python standard [`math`](https://docs.python.org/3.7/library/math.html) module like so:

```python
from math import pi # This should be the _first_ line of your file

pi
# => 3.141592653589793
```

</details>

Congrats on writing your first little Math program! Let's improve it a bit, as the output we get is a bit too raw. We would like to update the code so that the output looks like this:

```text
The radius is set to 5
Perimeter of the circle is 31.4
Area of the disk is 78.5
```

How can you do that? Talk with your buddy about the best strategy. This will help figure out the keywords to type in Google. Let's do it!

<details><summary markdown="span">Hint 1
</summary>

To round a number, you can use... the [`round()`](https://www.programiz.com/python-programming/methods/built-in/round) built-in method!

</details>

<details><summary markdown="span">Hint 2
</summary>

To build a complex string, the modern way of doing it in Python is to use something called **string interpolation** through [f-strings](https://www.programiz.com/python-programming/string-interpolation#f). By prefixing the opening quote of the string with an `f`, you can **inject Python code** directly _inside_ the string, thanks to curly braces `{}`.

</details>

### Function

Now that you have written a program using three variables, manipulating [integer, float numbers](https://snakify.org/en/lessons/integer_float_numbers/) and [strings](https://www.programiz.com/python-programming/methods/string), let's see how we can **refactor** the code to build a [**function**](https://www.programiz.com/python-programming/function). A function is a group of related statements that perform a specific task. Grouping those allow to **call** this function any time we need to perform that task.

The goal will be to take the code we already have and refactor it inside a function. The function's **signature** will be the following:

- The name of the function is `circle_math`
- The function takes one **parameter**, a `radius` (numeric value)
- The function **returns** a [`list`](https://www.programiz.com/python-programming/list) of two elements (floats): the computed perimeter and area based on the received parameter

Let's go step by step, at the bottom of your `playground.py` file, write the function definition, and make it return an _empty list_. Talk with your buddy, and if you are both stuck, you can have a look at the solution below.

<details><summary markdown="span">View solution
</summary>

Defining a function in Python requires to use the language keyword `def`, then the name of the function followed by parenthesis to declare how many **parameters** we need (can be 0, 1, etc.), and finally `:`. Once this is declared, you need to make a new line, and **indent** (use the `<TAB>` key on your keyboard!):

```python
def circle_math(radius):
    return []
```

As requested, the implementation of the function is just returning an empty list.

</details>

OK, now that the skeleton of the function is ready, try to implement it. How can you reuse the code from before? Do you need the `print` statement?

To test your code, you can use the following _after_ the definition of the function:

```python
# Copy-paste this code _after_ the `def circle_math...`

values = circle_math(5)
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")
```

Look at this code, see how we **call** the function? We just use its name, parenthesis and pass an **argument** (first time it's `5`, second time it's `6`). The function will get executed and return a value (a `list`!) that we store in a variable `values`. We then use this variable to actually print some information about the computed numbers.

N.B.: In this example, we **re-use** the variable `values`, meaning that the second time we call the `circle_math` function, the previous value stored in `values` is **overwritten**.

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/green_arrow_xr54uz.png) Run your code and make sure you get two lines describing math values for circles of radius 5 and 6. Don't hesitate to talk with your buddy or ask a TA.

:question: What's the difference between a parameter and an argument? Try to explain it to your buddy.

<details><summary markdown="span">View solution
</summary>

```python
from math import pi

def circle_math(radius):
    perimeter = 2 * pi * radius
    area = pi * radius * radius
    return [ perimeter, area ] # perimeter and area are called **local variables**
```

</details>

## Pushing your code to GitHub

Remember the steps we did in the previous _Hello World_ exercise to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `playground.py` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Playing around with Python`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window

That's it! Take a small break before diving into the `Fizz Buzz` exercise.
