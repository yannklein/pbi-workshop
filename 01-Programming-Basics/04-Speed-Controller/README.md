# Speed controller
The police hired you to create the brand new algorithm that calculates the amount of money a driver has to pay if he exceeds the speed limit.

According to the law, he must pay 5€ per km/h above the maximal authorized speed, with a minimal tax of 12.5€. (1)
Also, for every 10 km/h above the limit, the tax is doubled! (2)

For this exercise, you'll have to divide the problem in 3 functions to make a smooth and clear code.

Open `speed_controller.py` and solve this exercise by using functions with defined responsibilities.
Each one is specified with what we call a *docstring* delimited by 3 `'"'`. As usual tests are available to check your code.

## First step: multiplicator
The first function `multiplicator` will calculate by how much the tax will be multiplied regarding the (2) law.

<details><summary markdown='span'>View solution
</summary>

```python
def multiplicator(max_speed, actual_speed):
    return 2**((actual_speed - max_speed)//10)
```
</details>

## Second step: basic tax
The second function `basic_tax` will calculate the basic tax obtained regarding the (1) law. Remember that the minimal tax is 12.5€

<details><summary markdown='span'>View solution
</summary>

```python
def basic_tax(max_speed, actual_speed):
    delta = actual_speed - max_speed
    tax = delta*5
    if tax < 12.5:
        return 12.5
    return tax
```
</details>

## Last step: total tax
The last function `total_tax` will use the two previous function to calculate the total tax owed by the driver.

<details><summary markdown='span'>View solution
</summary>

```python
def total_tax(max_speed, actual_speed):
    tax = basic_tax(max_speed, actual_speed)
    mult = multiplicator(max_speed, actual_speed)
    return tax*mult
```
</details>

Once your function is working, you should still have a test not working. We are expecting you to handle the case where no infraction was committed.

If the maximal speed is greater than the actual_speed (= no infraction), you have to return `"no infraction committed"`.

<details><summary markdown='span'>View solution
</summary>
You need to add a condition to test which speed was the greatest.

```python
def total_tax(max_speed, actual_speed):
    if max_speed >= actual_speed:
        return "no infraction committed"
    tax = basic_tax(max_speed, actual_speed)
    mult = multiplicator(max_speed, actual_speed)
    return tax*mult
```
</details>

## Pushing your code to GitHub

Don't forget to use GitHub Desktop to push your progress!
