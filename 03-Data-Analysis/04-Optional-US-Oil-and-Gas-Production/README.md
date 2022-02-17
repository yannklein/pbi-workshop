# US Oil and Gas Production

In this exercise, we will analyze the US Oil & Gas production from June 2008 to June 2018. The dataset is [available on Kaggle](https://www.kaggle.com/djzurawski/us-oil-and-gas-production-june-2008-to-june-2018), and we already downloaded the CSVs in the exercise folder. They are located under the `data` subfolder, no need for you to download it again.

Open the Anaconda Prompt, and navigate to this exercise folder:

```bash
cd # Gets back to the $HOME directory
cd Documents/GitHub/python-beginners/03-Data-Analysis/04-Optional-US-Oil-and-Gas-Production
```

Once you are located in the right folder, you can list the files at your disposal:

```bash
dir
```

You can **launch the Notebook server** with:

```bash
jupyter notebook
```

Your browser should _automatically_ open Jupyter. If it doesn't, you can also launch Jupyter from Anaconda Navigator. Then head to your exercises' folder. You should see the exercise folder with `data`, `README.md`, etc. Click on the `Exercise.ipynb` link to open the notebook. This is where you will write notes & Python code. When analyzing data, we don't start with Spyder and write code, we stay in the notebook. Spyder will come later when we want to do some **Data Engineering** and create a script to be run at once.

In the Notebook exercises of today and the following days, you will go back & forth between these instructions and the Notebook where you will write the code. Have fun!

## Handling a notebook

This is your first Jupyter Notebook, a tool used by Data Analysts / Data Scientists to do two things:

- Analyse data with [`pandas`](https://pandas.pydata.org/) and plot with [`matplotlib`](https://matplotlib.org/)
- Take notes along the way to capture your train of thought

Notebooks are exploratory and differ from regular notes.

Here are the keyboard shortcuts you should start memorizing:

```
In Command Mode:
    A : Insert Cell Above
    B : Insert Cell Below
    D,D : Delete the Cell
    Y : Change cell to Python
    M : Change cell to Markdown (notes)
    ↩ : Enter Edition mode
In Edition Mode:
    ESC : Enter Command mode
    ⇧ + ↩ : Run the code / Save
H : Open Shortcuts cheat sheet.
```

Follow the instructions of the exercise, let's go!

## Name your Notebook

There should be a default code cell in your notebook, change its type to **Markdown** and copy-paste the following in it:

```markdown
## US Oil and Gas Production

Analysing the [Kaggle Dataset](https://www.kaggle.com/djzurawski/us-oil-and-gas-production-june-2008-to-june-2018) with information about Oil and Gas production in the US from June 2008 to June 2018.
```

Type `⇧ + ↩` to save and exit edit mode.

:question: What is **Markdown**? Take some time now to [read about it](https://guides.github.com/features/mastering-markdown/).

## Loading Modules

In the next code cell, copy paste the following:

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib
```

Type `⇧ + ↩` to **run** the code. It will be _remembered_ throughout the Jupyter Session (until you kill the `jupyter notebook` command in your terminal with `Ctrl+C`).

## Loading data from a CSV

Change the type of the last cell to Markdown and copy-paste the following in it:

```markdown
---

Let's load the Gas production:
```

Remember, a Jupyter notebook is not just about writing Python code, otherwise we would have stayed in Spyder!


Insert a cell below (code, the default) and write the two lines to load the **gas** consumption. Then visualize the `DataFrame` with the `.head()` function. When you are done, type `⇧ + ↩` to run the code.

```python
file = "data/U.S._natural_gas_production.csv"
gas_df = pd.read_csv(file, decimal=",")
gas_df.head(3)
```

Type `⇧ + ↩` to **run** the code. You should see the [**`head(n)`**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) of the DataFrame

There are some cells you might _always_ want to add just after having loaded a CSV file into a dataframe to get some insights about the **structure** and **size**:

```python
gas_df.shape
```

```python
gas_df.columns
```

```python
gas_df.dtypes[0:2] # Checking the types of the first two columns.
```

With this last one, we can see that the column `Month` is loaded as an `object` and **not** recognized as a date! We need to help Pandas a bit and do some post-load treatment on it. Let's do that in our next section:

## Converting the `Month` column to `datetime`

Open and read the documentation on [`pd.to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html). Insert a new code cell and try to **update** the `Month` column to a proper `datetime`.

⚠️ ⚠️ ⚠️ Please don't jump straight ahead to the solution! Take some time to read the documentation and experiment in your Jupyter notebook!

<details><summary markdown='span'>View solution
</summary>

```python
gas_df['Month'] = pd.to_datetime(gas_df['Month'], format='%Y-%m-%d')
gas_df.head(3)
```

```python
gas_df.dtypes[0:2] # To check if this worked!
```

The format is here to guide Pandas when reading the column. Depending on the input you get, you might have something like `%d-%m-%Y` or even `%m/%d/%Y`. You job as a developer is to identify the pattern by looking at the raw data from the CSV.

</details>

Once you've done that, you can treat the values inside the column `Month` as `datetime` object:

```python
gas_df['Month'].dt.year.head()
```

```python
gas_df['Month'].dt.month.tail()
```

## Grouping rows

As we are starting a new block of exploration, insert a **Markdown** cell and append the following code:

```markdown
---

## Yearly Gas production
```

Now that we have prepared the dataframe, we can try to answer a first Business-related question:

> How much gas has been produced yearly globally and in every state of the US?

To answer this question, we need to **aggregate** the rows based on the year of the `Month` column. Go ahead, insert a new code cell and code this aggregation using [`DataFrame.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [`DataFrame.sum()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html).

<details><summary markdown='span'>View solution
</summary>

```python
yearly_gas_df = gas_df.groupby(gas_df['Month'].dt.year).sum()
yearly_gas_df
```

</details>

Once we have this aggregated dataframe, time to **plot** the total production in the `U.S.` thanks to the [`DataFrame.plot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) functions.

<details><summary markdown='span'>View solution
</summary>

We can quickly plot the `U.S.` column (total production) of this aggregated dataframe with the following line:

```python
plot = yearly_gas_df[['U.S.']].plot(kind="bar")
plot.set_xlabel("Year")
```

</details>

## Discarding rows with Boolean Indexing

In the previous section, we've seen that the production data are not complete for the year 2008 and 2018 (we only have half of the year). We'd like to continue working with full years, meaning we need to discard the first and last rows of `yearly_gas_df` based on the year.

We are going to look at the **index** of the DataFrame, and build a boolean condition using [`np.logical_and`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_and.html):

```python
np.logical_and(yearly_gas_df.index >= 2009, yearly_gas_df.index <= 2017)
```

How can you use this [`np.ndarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html) and [**boolean indexing**](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing) to keep only the full years in `yearly_gas_df`? Can you plot it?

<details><summary markdown='span'>View solution
</summary>

```python
full_years = np.logical_and(yearly_gas_df.index >= 2009, yearly_gas_df.index <= 2017)
full_yearly_gas_df = yearly_gas_df[full_years]
plot = full_yearly_gas_df[['U.S.']].plot(kind="bar")
plot.set_xlabel("Year")
```

</details>

## Plotting several columns

Let's now create a new section in our Notebook to analyze the Gas production of different states in the U.S. First, let's insert a **Markdown** cell:

```markdown
### State production

Let's have a look at the yearly production of some specific states
```

Then let's have a look at the available states, looking at all the columns _except_ the first one:

```python
full_yearly_gas_df.columns[1:].sort_values()
```

:question: Can you insert a new cell and write the code to plot linecharts of the gas production of four states of your choice? You can start from the `full_yearly_gas_df` dataframe.

<details><summary markdown='span'>View solution
</summary>

If we pick Colorado, Louisiana, Ohio and Utah, this is how we can do it:

```python
plot = full_yearly_gas_df[['Colorado', 'Louisiana', 'Ohio', 'Utah']].plot()
plot.set_xlabel("Year")
```

</details>

## Loading a second CSV

The Kaggle dataset we are using does not only have information about the gas production, there is also some about the **crude oil** one. Create a new section in your Notebook with the following Markdown cell:

```markdown
---

## Comparing with Crude Oil Production
```

Create a new dataframe for the oil:

- Load it with the [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function
- Parse the `Month` column into a `datetime` object

<details><summary markdown='span'>View solution
</summary>

```python
file = "data/U.S._crude_oil_production.csv"
oil_df = pd.read_csv(file)
oil_df['Month'] = pd.to_datetime(oil_df['Month'], format='%Y-%m-%d')
oil_df.head()
```

</details>

Then create two dataframes `yearly_gas` and `yearly_oil` by grouping by year, summing and filtering the **global** production for both commodities. [Rename the columns](https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas) to `Gas` and `Crude oil`.


<details><summary markdown='span'>View solution
</summary>

You need to create 2 cells:

```python
yearly_gas = gas_df.groupby(gas_df['Month'].dt.year).sum()[['U.S.']]
yearly_gas.columns = [ 'Gas' ]
yearly_gas.head(3)
```

```python
yearly_oil = oil_df.groupby(oil_df['Month'].dt.year).sum()[['U.S. Crude Oil']]
yearly_oil.columns = [ 'Crude Oil' ]
yearly_oil.head(3)
```

</details>

Now that you have those two dataframes, create one by concatenating both. Store this new dataframe into a `yearly_merged` variable. You should use the [`pd.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html), and don't forget to set the `axis` parameter!

<details><summary markdown='span'>View solution
</summary>

```python
yearly_merged = pd.concat([yearly_oil, yearly_gas], axis='columns')
yearly_merged
```
</details>

Finally, plot the `yearly_merged` dataframe and try to set the legend to include the units advertised in the original [Kaggle dataset](https://www.kaggle.com/djzurawski/us-oil-and-gas-production-june-2008-to-june-2018).

<details><summary markdown='span'>View solution
</summary>

```python
plot = yearly_merged.plot(kind="bar")
plot.set_xlabel("Year")
plot.legend(['Gas (Millions of Cubic feet)', 'Crude Oil (Thousands of barrels)'])
```

</details>

That's it, congratulations on completing your first Data Analysis through a Jupyter Notebook 👏 🚀

## Pushing your code to GitHub

Remember the steps we did in the two first days to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `Exercise.ipynb` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Complete my first Data Analysis with Jupyter Notebook`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window

That's it! Take a small break before diving into the next exercise.
