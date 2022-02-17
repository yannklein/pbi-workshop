# Math for Dummies

## Testing

Some of this week's exercises will be done using [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD for short). That's a technique where developers start by writing a test for the function they want to implement. They imagine a scenario where they _already know the answer_, and write a test (some code) calling this method with some arguments. Then they check if the result returned by the function (still to be coded!) is equal to the value they expect. If yes, the test passes, it's green, otherwise the test fails, it's red. Of course, in TDD, the first time you run the test, it's red as you haven't coded the function yet!

We will use this technique but in a simplified fashion as you are learning to code. The tests are **already written** in the `test_math_for_dummies.py` file by the teaching team. You can benefit from TDD without writing the tests yourself, hurray!

Go ahead and open the `math_for_dummies.py` file in Spyder.

You can see we want you to implement two function. One that will take two parameter and return the **sum** of both, and another one which returns the **multiplication** of both.

Before you write a single line of code, let's **run the tests** a first time. Just run the file containing the tests as you would for any other script.

The test will run and check the code. It takes less than a second:

![](https://res.cloudinary.com/wagon/image/upload/v1583774693/spyder_run_tests_all_red_yaisqg.jpg)

All tests are failing! That's quite normal, as you haven't implemented the code yet. Go ahead and try to implement the `summify` method. Run the tests from time to time to check your result.

<details><summary markdown="span">Stuck? View solution
</summary>

The `summify` function takes two parameter and should **return** the sum of both. In Python, we can write it like this:

```python
def summify(x, y):
    return x + y
```

Beware of **indentation**, in Python it's very important! The code inside the function (what's after the `:` on a new line) has to be indented. We use the `TAB` key on the keyboard to do so.

</details>

Once you've got the code right, if you run the tests you should see that the number of failures decreased:

![](https://res.cloudinary.com/wagon/image/upload/v1583774693/spyder_run_tests_some_green_aokkca.jpg)

Awesome! Now try to do the same with the other method to make it run **without failures**.

### Where are the tests?

Surely, you must be proud of having written code and passed the tests! You will see that this failed-passed cycle is very addictive and might trigger a dopamine release in your brain :wink:

You must also wonder why there are 6 tests, and **where** they are. It's not magic, go ahead and open the `test_math_for_dummies.py` file. You can read the tests out loud, it's quite straightforward:

![](https://res.cloudinary.com/wagon/image/upload/v1562058694/spyder_show_tests_nd0sid.png)

### Bonus: Pylint

Python comes with a code analysis tool ([Pylint](https://www.pylint.org/)) to help write better Python by providing you with **style** feedback. You can use this [feature right from Spyder](https://docs.spyder-ide.org/pylint.html) like this:

![](https://res.cloudinary.com/wagon/image/upload/v1562058694/spyder_pylint_pou9tp.png)

Try to run it from time to time on your code, it will give you hints on coding standard, error detection, refactoring help, etc.

## Pushing your code to Github
Once again we will show you how to save your work online.

Open GitHub Desktop, and go to the `python-beginners` project. You should see something close to the following:

![](https://res.cloudinary.com/wagon/image/upload/v1562523652/github-desktop-first-commit-python-beginners_sjwg0m.png)

On the left of the screen, you can see the files you have changed since the latest snapshot of your code. You can tick/untick the file to include it in the next snapshot we are preparing. Usually, you tick everything. A nice feature is that you can click on each file and see on the right the **diff** between the previous snapshot and now. Very easy to spot your progress or errors!

To finalize saving your work (i.e. creating a **commit**), we need to fill the form at the bottom left of the GitHub Desktop window. You can proceed as follow:

- Fill the title (first input) with `Solve exercise Math for Dummies`
- Leave the description blank
- Click on the blue button which says "Commit to **`master`**"

Finally, we need to **push this commit to GitHub** as for now it just exists on your computer. Look at the top of the GitHub Desktop window, you should see a :up_arrow: **Push origin** button. Click on it!

To view your work, you can now head over to GitHub and look at your [latest commits](https://github.com/<user.github_nickname>/python-beginners/commits/master) on the `python-beginners` repository. Can you see it? Congratulations 🎉! You can't? Ask a TA!
