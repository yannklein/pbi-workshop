# COVID-19 data

In this exercise, we will analyze a dataset of the COVID-19 disease to get a lot of different information. The dataset is downloaded CSVs in the exercise folder. No need for you to download it again.

Open the Anaconda Prompt, and navigate to this exercise folder:

```bash
cd # Gets back to the $HOME directory
cd Documents/GitHub/python-beginners/03-Data-Analysis/01-COVID
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
## COVID-19 data

Analysing a dataset with information about the COVID-19.
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

Let's load COVID-19 datas:
```

Remember, a Jupyter notebook is not just about writing Python code, otherwise we would have stayed in Spyder!


Insert a cell below (code, the default) and write the two lines to load the **COVID-19** data. Then visualize the `DataFrame` with the `.head()` function. When you are done, type `⇧ + ↩` to run the code.

```python
file = "covid_19_data.csv"
covid_df = pd.read_csv(file, ",")
covid_df.head(3)
```

Type `⇧ + ↩` to **run** the code. You should see the [**`head(n)`**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) of the DataFrame

There are some cells you might _always_ want to add just after having loaded a CSV file into a dataframe to get some insights about the **structure** and **size**:

```python
covid_df.shape
```

```python
covid_df.columns
```

```python
covid_df.dtypes
```

With this last one, we can see that the column `Date` is loaded as an `object` and **not** recognized as a date! We need to help Pandas a bit and do some post-load treatment on it. Let's do that in our next section:

## Converting the `Date` column to `datetime`

Open and read the documentation on [`pd.to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html). Insert a new code cell and try to **update** the `Date` column to a proper `datetime`.


⚠️ ⚠️ ⚠️ Please don't jump straight ahead to the solution! Take some time to read the documentation and experiment in your Jupyter notebook!

<details><summary markdown='span'>View solution
</summary>

To convert a `Object` into a you have to do it this way:
```python
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format="%Y-%m-%d")
```

```python
covid_df.dtypes
```

The format is here to guide Pandas when reading the column. Depending on the input you get, you might have something like `%d-%m-%Y` or even `%m/%d/%Y`. You job as a developer is to identify the pattern by looking at the raw data from the CSV.

</details>


Once you've done that, you can treat the values inside the column `Date` as `datetime` object:

```python
covid_df['Date'].dt.year.head()
```

```python
covid_df['Date'].dt.month.tail()
```

## Grouping Rows

As we are starting a new block of exploration, insert a **Markdown** cell and append the following code:

```markdown
---

## Monthly Covid Deaths
```

Now that we have prepared the dataframe, we can try to answer a first question:

> What was at the end of each month the amount of deaths due to the COVID-19?

To answer this question you have to look closely to how the `Deaths` column is constructed. The data are sorted by date and country name but they didn't registered how many deaths there was by day.  

Indeed the `Deaths` columns is **cumulative**, it means that one row contains the information that we need.
We're going to work step by step to achieve this question.

1. First of all we want the amount of deaths of each months, so we have to create a new dataframe in which the `Date` column will only contain the months. Pay attention we don't want to modify the original dataframe.

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_df = covid_df.copy()
monthly_covid_df['Date'] = monthly_covid_df['Date'].dt.month
```
</details>

2. Now that we have our correct dataframe, we have to rearrange it to get only the rows that contains the last value of each area for each month.
To do so the easiest way is to first sort the dataframe by deaths (ascending order) and then delete all duplicates rows that are useless information for us.

Here are the two methods that you need to use : [`Dataframe.sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) and [`Dataframe.drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)

Be sure to correctly read and understand the documentation before jumping into the exercise.

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_df.sort_values(by=['Deaths'], inplace=True)
monthly_covid_df.drop_duplicates(['Province/State', 'Country/Region', 'Date'], keep='last', inplace=True)
```
</details>

3. As a last step you'll have to **aggregate** the rows based on the month of the `Date` column. Go ahead, insert a new code cell and code this aggregation using [`DataFrame.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [`DataFrame.sum()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html).

<details><summary markdown='span'>View solution
</summary>

```python
monthly_deaths = monthly_covid_df.groupby(monthly_covid_df['Date'])['Deaths'].sum()
monthly_deaths
```

</details>

Create a new Dataframe that answer to the same question as previously, but only with the deaths in France:

> What was at the end of each month the amount of deaths in France due to the COVID-19 ?

Be sure to follow the same steps as previously
<details><summary markdown='span'>View solution
</summary>

```python
monthly_france_df = covid_df.copy()
monthly_france_df.Date = monthly_france_df.Date.dt.month
monthly_france_df = monthly_france_df[monthly_france_df["Country/Region"] == "France"]
monthly_france_df.sort_values(by=['Deaths'], inplace=True)
monthly_france_df.drop_duplicates(['Province/State', 'Country/Region', 'Date'], keep='last', inplace=True)
monthly_france_deaths_df = monthly_france_df.groupby(monthly_france_df['Date'])['Deaths'].sum()
monthly_france_deaths_df
```

</details>

Once we have this aggregated dataframe, time to **plot** the monthly deaths due to covid-19 in the whole world thanks to the [`DataFrame.plot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) functions.

<details><summary markdown='span'>View solution
</summary>

We can quickly plot the monthly deaths due to covid-19 in the whole world of this aggregated dataframe with the following line:

```python
plot = monthly_deaths.plot(kind="bar")
plot.set_xlabel("Month")
```

</details>

## Discarding rows with Boolean Indexing

In the previous section we displayed covid death from january to july, but what if we want to know the deaths amount when the disease was at its peak. We'd like to discard the months that are not between february (2) and june (6).

We are going to look at the **index** of the DataFrame, and build a boolean condition using [`np.logical_and`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_and.html):

```python
np.logical_and(monthly_deaths.index > 1, monthly_deaths.index < 7)
```

How can you use this [`np.ndarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html) and [**boolean indexing**](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing) to keep only the interesting years in `peak_monthly_deaths`? Can you plot it?

<details><summary markdown='span'>View solution
</summary>

```python
peak_monthly_deaths = monthly_deaths[np.logical_and(monthly_deaths.index > 1, monthly_deaths.index < 7)].copy()
plot = peak_monthly_deaths.plot(kind="bar")
plot.set_xlabel("Month")
```

</details>

## Compare France and United Kingdom confirmed cases

We're now going to separate the `covid_df` (original) Dataframe in two.
We're going to put the France and UK datas in two different Dataframe containing only those columns: Date, Country, Confirmed and Deaths

Don't hesitate to use the code that you already wrote for France, you'll have to do the same for UK. Indeed the `Confirmed` column works exactly the same as the `Deaths` column (cumulative).

<details><summary markdown='span'>View solution
</summary>
France:

```python
monthly_france_cases_df = monthly_france_df[['Date', 'Country/Region', 'Confirmed', 'Deaths']]
monthly_france_cases_df
```
UK:

```python
monthly_uk_df = covid_df.copy()
monthly_uk_df.Date = monthly_uk_df.Date.dt.month
monthly_uk_df = monthly_uk_df[monthly_uk_df["Country/Region"] == "United Kingdom"]
monthly_uk_df.sort_values(by=['Confirmed'], inplace=True)
monthly_uk_df.drop_duplicates(['Country/Region', 'Date'], keep='last', inplace=True)
monthly_uk_cases_df = monthly_uk_df[['Date', 'Country/Region', 'Confirmed', 'Deaths']]
monthly_uk_cases_df
```
</details>

Now group the confirmed cases by `Date` and plot the result in the same graph

<details><summary markdown='span'>View solution
</summary>
France:

```python
monthly_france_confirmed_df = monthly_france_cases_df.groupby(monthly_france_cases_df["Date"]).sum()["Confirmed"]
monthly_france_confirmed_df
```

UK:

```python
uk_confirmed_monthly = monthly_uk_df.groupby(monthly_uk_df["Date"]).sum()["Confirmed"]
uk_confirmed_monthly
```

Plot:

```python
ax = monthly_france_confirmed_df.plot(figsize=(12,4))
uk_confirmed_monthly.plot(ax=ax)
```
</details>

## Pushing your code to GitHub

Remember the steps we did in the two first days to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `Exercise.ipynb` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Complete my first Data Analysis with Jupyter Notebook`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window

That's it! Take a small break before diving into the next exercise.
