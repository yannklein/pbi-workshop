# Text Extraction with Regex

In this exercise we are going to use **Regular Expression** in order to extract data from a plain text file.<br>

The text file path is `03-Text-Extraction-with-Regex/data/receipts.txt`.

The receipts in this file are from a **restaurant**. Each receipt gives us how many plates were served and how much money the restaurant made that day.

If we open the file we can see how the receipts are stored:
<br>
<img src="https://res.cloudinary.com/wagon/image/upload/v1562063870/Receipts_snapshot_dddner.png" alt="Receipts_snapshot.png" height="400" style="box-shadow: 0 0 25px -15px #88b">

Before we start working with the receipts let's talk about **Regular Expressions**. We will need them to extract the **dates**, the **total amount** and the **quantity** fields from the *receipts.txt*.

## Part 1: Working with Regex

First, we need to create a new notebook and make the usual imports:

```python
import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib

```

To use **regex** in our notebook we will also need to import the regex library:

```python
import re
```

### Intro to Regex

OK, so let's say you have the following text:

```python
"Hello my name is Sebastien, you can call me on 0664533519. See you!"
```

You want to **extract** the number from this text (unstructured data). That's _exactly_ what Regex are useful for!<br>
Regex are strings that define a **search pattern**.
So here the Regex would be:

```python
r"\d{10}"
```

`r""` is the syntax for a string that will be used as Regex.<br>
`\d` match a character that represents any **decimal digit** `[0,1,2..8,9]`<br>
`{10}` match exactly 10 _consecutive_ occurence of the **previous character** (here `\d`, any digit)

So now we will search in our string any match with this Regex.<br>
We can use `re.findall(pattern, string)` to do that:
[re.findall( ) documentation](https://docs.python.org/2/library/re.html#re.findall)

```python
# TEST THIS IN YOUR NOTEBOOK
pattern = r"\d{10}"
text_to_search = "Hello my name is sebastien, you can call me on 0664533519. See you!"
re.findall(pattern, text_to_search)
```
----
**Your turn now!** Try to find the right Regex to find the **ZIP code** in this string:

```python
"I moved to Paris 75011, it's closer to my workplace."
```

<details><summary markdown='span'>View solution
</summary>


```python
pattern = r"\d{5}"
text_to_search = "I moved to Paris 75011, it's closer to my workplace."
re.findall(pattern, text_to_search)
```
</details>

### Words with regex
With regex, you can also search for words like this:

```python
# TEST THIS IN YOUR NOTEBOOK
pattern = r"date of"
text_to_search = "The date of creation is 2019/03/12 and date of expiration is 2021/03/01"
re.findall(pattern, text_to_search)
```

<details><summary markdown='span'>Result
</summary>

You should find two matches.
```python
['date of', 'date of']
```

</details>

### Words mixed with digits
You can also _mix_ letters or word with a **token** like `\d`. For example, if we want to match the dates we can use:

```python
# TEST THIS IN YOUR NOTEBOOK
pattern = r"\d{4}/\d{2}/\d{2}"
text_to_search = "The date of creation is 2019/03/12 and date of expiration is 2021/03/01"
re.findall(pattern, text_to_search)
```

<details><summary markdown='span'>Result
</summary>

You should find two matches.
```python
['2019/03/12', '2021/03/01']
```

</details>

**Your turn!** Find the Regex that matches the date in this string from the receipt:

```python
"Receipt Number 103402 ||| 15-02-2017"
```

You can play around with the Regex on this website: [regex101.com](https://regex101.com/r/eudk0M/1)

<details><summary markdown='span'>Solution
</summary>

```python
pattern = r"\d{2}-\d{2}-\d{4}"
text_to_search = "Receipt Number 103402 ||| 15-02-2017"
re.findall(pattern, text_to_search)
```

</details>

### Token and Quantifier

**Token** can either be a character like `a` or a character in a larger set, like `3` or `9` in the set `\d`.
<br>
The most common token:

- `a`, `4`, `@`... Matches the exact **same character**.
- `\d`          Matches any **decimal digit**. Equivalent to _[0-9]_.
- `\w`          Matches any **letter, digit or underscore**. Equivalent to *[a-zA-Z0-9_]*.
- `\s`          Matches any **space, tab or newline** character.
- `.`           Matches **any character** other than newline

Tokens can work in pair with quantifiers.<br>
**Quantifiers** specify how often a preceding element is allowed to occur, just like we did in this Regex:

```python
r"\d{10}"
```

The most common quantifiers:

- `?` The question mark indicates **zero or one** occurrences of the preceding element. For example, colou?r matches both "color" and "colour".
- `*` The asterisk indicates **zero or more** occurrences of the preceding element. For example, ab*c matches "ac", "abc", "abbc", "abbbc", and so on.
- `+` The plus sign indicates **one or more** occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".
- `{n}` The preceding item is matched exactly **n** times.

---

### Exercices
Now let's try to match the **"Quantity"** line in a receipt.<br>
Go to this page and find the right pattern: [regex101.com](https://regex101.com/r/DRY159/1)

<details><summary markdown='span'>Solution
</summary>

```python
r"Quantity +\d+"
```

</details>

Next, find the pattern that matches the full **"Total Amount"** line.<br>
Go to this page and find the right pattern: [regex101.com](https://regex101.com/r/DRY159/1)

<details><summary markdown='span'>Solution
</summary>

```python
r"Total Amount +\d+.\d{2} €"
```

</details>

Great! We now have a way to get the right line.
<br>But it would be even better if we could extract **only the numerical value** from the line.
<br>To do that we will need **groups**!

### Groups

Groups are a way to select only a part of the match. Groups are delimited by parenthesis like `(\d+)`.

Here is an exemple:

```python
# TEST THIS IN YOUR NOTEBOOK
pattern = r"Receipt Number (\d+)"
text_to_search = "Receipt Number 103402 ||| 15-02-2017"
re.findall(pattern, text_to_search)
```

<details><summary markdown='span'>Result
</summary>

You should only get the value of the group.
```python
['103402']
```

</details>

**Your turn!**<br>
Find the right grouping to get only the **"Quantity"** value: [regex101.com](https://regex101.com/r/DRY159/1)

<details><summary markdown='span'>Solution
</summary>

```python
r"Quantity +(\d+)"
```

</details>

Find the right grouping to get only the **"Total Amount"** value: [regex101.com](https://regex101.com/r/DRY159/1)

<details><summary markdown='span'>Solution
</summary>

```python
r"Total Amount +(\d+.\d{2}) €"
```

</details>

---

🎉Awesome! You now know everything you need to know to get the **dates**, the **total amount** and the **quantity** values from the receipts.

## Part 2: From a text file to a DataFrame

What we want to do:

 1. **Read** the receipt text file
 2. Create a **list** with the receipts
 3. Prepare a **dictionary** where we will save our data
 4. **Iterate** over each receipt
    - *Find the data* we want with a regex
    - *Add those data* to our dictionary
 5. Create a **dataframe** from this dictionary

### 1. Read the receipt text file

To read a file with python you have to use `open()` like this:

```python
filepath = "data/receipts.txt"
with open(filepath) as f:
    receipts_str = f.read()
```

And you can print the beginning of the file with:

```python
print(receipts_str[:500])
```

Do that in your notebook and make sure you can see some receipt.

### 2. Create a list with the receipts

To create a list of all the receipts we need to find the **delimiter** between the receipts.<br>
So look at what you previously printed and choose a delimiter.<br>
You can now use `split()` on your string to get the list of all the receipts, the list should contain **100 items**.

<details><summary markdown='span'>Solution
</summary>

```python
receipts_list = receipts_str.split("====================================")
len(receipts_list)
```

</details>


### 3. Prepare a dictionary where we will save our data

Before we start **iterating** over array we need a dictionary to save the data we found.
The format we want for this is:

```python
receipts_dict = {
    "date": [],
    "quantity": [],
    "total_amount": []
}
```

And it should like this once filled with data:

```python
receipts_dict
=> {
    "date": ['22-10-2017','23-10-2017','26-10-2017',...],
    "quantity": [123, 232, 134, ...],
    "total_amount": [1234.53, 1563.30, 2345.00, ...]
   }
```

### 4. Iterate over each receipt

Ok let's start iterating!<br>
You can first **print each receipt** in order to know what we are dealing with.

<details><summary markdown='span'>Solution
</summary>

```python
for receipt in receipts_list:
    print(receipt)
```

</details>

### 4.1. Find the data we want with some Regex

Now it's time to use our Regex knowledge to get the **dates**, the **total amount** and the **quantity** values from the current receipt.

<details><summary markdown='span'>Date Solution
</summary>

```python
for receipt in receipts_list:
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    date = re.findall(date_pattern, receipt)[0]
```

</details>

<details><summary markdown='span'>Total Amount Solution
</summary>

```python
for receipt in receipts_list:
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    date = re.findall(date_pattern, receipt)[0]
    total_amount_pattern = r"Total Amount +(\d+.\d{2}) €"
    total_amount = re.findall(total_amount_pattern, receipt)[0]
```

</details>

<details><summary markdown='span'>Quantity Solution
</summary>

```python
for receipt in receipts_list:
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    date = re.findall(date_pattern, receipt)[0]
    total_amount_pattern = r"Total Amount +(\d+.\d{2}) €"
    total_amount = re.findall(total_amount_pattern, receipt)[0]
    quantity_pattern = r"Quantity +(\d+)"
    quantity = re.findall(quantity_pattern, receipt)[0]
```

</details>

If you add this line to your loop you should see all the data you found.

```python
    print(f"date: {date}, total_amount: {total_amount}, quantity: {quantity}")
```

```
=>
    date: 02-01-2017, total_amount: 3097.00, quantity: 3097.00
    date: 05-01-2017, total_amount: 935.00, quantity: 935.00
    date: 23-01-2017, total_amount: 2808.00, quantity: 2808.00
    date: 31-01-2017, total_amount: 4368.00, quantity: 4368.00
    date: 06-02-2017, total_amount: 1988.50, quantity: 1988.50
        ...
```

### 4.2. Add these value to our dictionary

We can now `append()` each value in the right list of the dictionary.


<details><summary markdown='span'>Solution
</summary>

```python
for receipt in receipts_list:
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    date = re.findall(date_pattern, receipt)[0]
    total_amount_pattern = r"Total Amount +(\d+.\d{2}) €"
    total_amount = re.findall(total_amount_pattern, receipt)[0]
    quantity_pattern = r"Quantity +(\d+)"
    quantity = re.findall(quantity_pattern, receipt)[0]
    receipts_dict["date"].append(date)
    receipts_dict["total_amount"].append(total_amount)
    receipts_dict["quantity"].append(quantity)
```
</details>

Before going to the next step make sure your dictionary look something like this:

```python
# The way its printed might be a bit different on your computer
receipts_dict
=> {
    "date": ['22-10-2017','23-10-2017','26-10-2017',...],
    "quantity": [123, 232, 134, ...],
    "total_amount": [1234.53, 1563.30, 2345.00, ...]
   }
```

### 5. Create a dataframe from this dictionary

Finally, you can just convert this dictionary to a **DataFrame** with pandas.<br>
You can look at this documentation if you don't remember the syntax: [pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html)

<details><summary markdown='span'>Solution
</summary>

```python
receipts_df = pd.DataFrame.from_dict(receipts_dict)
receipts_df.head()
```
</details>


------

👌**Nice !** Now we can start analyzing our DataFrame.

## PART 3: Data visualization
### 1. Replace date string by datetime object

Before we start plotting our data in any way we should convert our date **from string to DateTime** object.
With DateTime we will be able to **sort** our data.

To do the conversion you can use `Pandas.to_datetime()`

[pd.to_datetime documentation](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
[Format documentation](http://strftime.org/)

<details><summary markdown='span'>Solution
</summary>

```python
receipts_df['date'] = pd.to_datetime(receipts_df['date'], format="%d-%m-%Y")
```
</details>

You can also **sort and save** your DataFrame.

<details><summary markdown='span'>Solution
</summary>

```python
receipts_df.sort_values('date', inplace=True)
```
</details>

### 2. Set the date column as the index

You can use the DataFrame method `set_index()`

[documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
<details><summary markdown='span'>Solution
</summary>

```python
receipts_df = receipts_df.set_index('date')
```
</details>

### 3. Convert strings to floats

At this point, if we do a `receipts_df.info()` we see that we still have strings in our columns **quantity** and **total_amount**.
<br>In order to print some plots we need to convert "quantity" and "total_amount" to float.

To do the conversion you can use `pandas.to_numeric()`

`pandas.to_numeric()` documentation: [pandas.pydata.org](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html)


<details><summary markdown='span'>Solution
</summary>

```python
receipts_df["quantity"] = pd.to_numeric(receipts_df["quantity"])
receipts_df["total_amount"] = pd.to_numeric(receipts_df["total_amount"])
```
</details>

### 4. Plot the total_amount column

Ok, now we can start **exploring** and **plotting** our data.
<br>
Let's see the evolution of the **"total_amount"**!

<details><summary markdown='span'>Solution
</summary>

```python
receipts_df['total_amount'].plot(figsize=(14,5))
```
</details>

### 🎉 Congratulation! You now know how to work with "unstructured data"
