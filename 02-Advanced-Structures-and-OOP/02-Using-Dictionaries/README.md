# Using dictionaries: Tricount with dictionaries
[Tricount](https://www.tricount.com/) is an application that allows you to calculate and keep traces of the amount of money spent by each member of a group.
For example if you go on vacation with your friends, you can create a tricount to know who paid for the supermarket shopping each day. It will then tell you who needs to refund who and which amount to refund.

Today, we're going to work with a brand new data structure and create an easy version of a tricount (money manager in a group of person).
In Python, there is one data structure that is really indicated to deal with the tricount exercise : a Python [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

So first of all, we're going to compare dictionaries with another data structure that you've already used: lists.
To make a tricount with the list data structure we would have to use the following nested list:
```python
tri_count = [['Eric', 0], ['Tanguy', 40], ['Lucile', 0], ['Michael', 20]]
```
Can you spot the difference between lists and dictionaries and understand why using a dictionary is a better approach for the tricount exercise?

How would you convert this `tri_count` nested list in a `tri_count_dic` dictionary?
- What are the keys? What type are they?
- What are the values? What type are they?
<details><summary markdown='span'>View solution
</summary>

```python
tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
```
The key of the tricount dictionary will be the username (`str`) and the values their amount of money spent (`int`).
</details>

You can copy/paste this dictionary in `program.py`, it will help you to test your functions later.

## Exercises
In the `program.py` file you'll find a scenario written in *pseudo code* which is a bunch of small exercises to make yourself comfortable with dictionaries and calling functions.
The first thing you have to do is to copy and past your `tri_count_dic` in `program.py`.

Now, let's switch to `tricount.py`. A few functions are already defined in the file, fill them so that you can use them in the `program.py` script afterwards. Once it's done, use your newly defined functions to solve and run `program.py` by completing the scenario.

Every function can also be tested with the script `test_tricount.py`.

For the fastest of you an optional question is also available regarding a smarter debts distribution of the amount recorded in the tricount dictionary.

## Pushing your code to GitHub

Don't forget to use GitHub Desktop to push your progress!
