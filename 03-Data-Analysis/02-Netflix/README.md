# Netflix Movies and TV shows

In this exercise, we will analyze all Movies and TV shows that are available on Netflix's platform. The dataset is [available on Kaggle](https://www.kaggle.com/shivamb/netflix-shows), and we already downloaded the CSVs in the exercise folder.

Open the Anaconda Prompt, and navigate to this exercise folder:

```bash
cd # Gets back to the $HOME directory
cd Documents/GitHub/python-beginners/03-Data-Analysis/02-Netflix
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
## Netflix Movies and TV shows

Analysing the [Kaggle Dataset](https://www.kaggle.com/shivamb/netflix-shows) with information about Netflix Movies and TV shows.
```

Type `⇧ + ↩` to save and exit edit mode.

:question: What is **Markdown**? Take some time now to [read about it](https://guides.github.com/features/mastering-markdown/).

Remember, a Jupyter notebook is not just about writing Python code, otherwise we would have stayed on _Spyder_, add notes!

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

Let's load Netflix datas:
```

Remember, a Jupyter notebook is not just about writing Python code, otherwise we would have stayed in Spyder!


Insert a cell below (code, the default) and write the two lines to load the **Netflix** data. Then visualize the `DataFrame` with the `.head()` function. When you are done, type `⇧ + ↩` to run the code.

```python
file = "netflix_titles.csv"
netflix_df = pd.read_csv(file, ",")
netflix_df.head(3)
```

Type `⇧ + ↩` to **run** the code. You should see the [**`head(n)`**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) of the DataFrame

There are some cells you might _always_ want to add just after having loaded a CSV file into a dataframe to get some insights about the **structure** and **size**:

```python
netflix_df.shape
```

```python
netflix_df.columns
```

```python
netflix_df.dtypes
```

With this last one, we can see that the column `Date` is loaded as an `object` and **not** recognized as a date! We need to help Pandas a bit and do some post-load treatment on it. Let's do that in our next section:

## Converting the `date_added` column to `datetime`

Open and read the documentation on [`pd.to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html). Insert a new code cell and try to **update** the `date_added` column to a proper `datetime`.


⚠️ ⚠️ ⚠️ Please don't jump straight ahead to the solution! Take some time to read the documentation and experiment in your Jupyter notebook! 

Moreover `date_added` column may need a little modification to work properly :wink: .

<details><summary markdown='span'>View solution
</summary>

To convert an `Object` into a `Datetime` object you have to do it this way:

```python
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format="%B %d, %Y")
```

By doing this you normally should get an error because there are some date that have been encoded with a leading space.
Try to find on internet how you can delete all leading space in all strings of a pandas column.

```python
netflix_df.dtypes
```

The format is here to guide Pandas when reading the column. Depending on the input you get, you might have something like `'%d-%m-%Y'` or even `'%m/%d/%Y'`. Here the date format was `'%B %d, %Y'` and even `' %B %d, %Y'` for some case. At the end you need to be able to adapt to every situation event if it is not your fault that the data are messy. You job as a developer is to identify the pattern by looking at the raw data from the CSV.

</details>

<details><summary markdown='span'>Hint
</summary>
    
The pandas [`strip()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html) function should be helpful to remove leading spaces.
</details>


<details><summary markdown='span'>View solution
</summary>

To remove all leading (and trailing) spaces:

```python
netflix_df['date_added'] = netflix_df['date_added'].str.strip()
```
then use to_datetime to convert the `date_added` column:

```python
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format="%B %d, %Y")
```

```python
netflix_df.dtypes
```
</details>


## Netflix movies

As we are starting a new block of exploration, insert a **Markdown** cell and add a title.

Our dataframe is now ready, we can look for specific data in it. We're going first to create a new dataframe containing only the movies available on Netflix (remember we don't want to modify the original dataframe).

<details><summary markdown='span'>View solution
</summary>

```python
netflix_movies_df = netflix_df[netflix_df["type"] == "Movie"].copy()
```
</details>

### Duration

Now convert the string value of the `duration` column into its integer version. Pay attention, there are movies that are only 3 min long ;-).

E.g.: '90 min' -> 90

<details><summary markdown='span'>View solution
</summary>

```python
netflix_movies_df['duration'] = netflix_movies_df['duration'].str.split(" ")
netflix_movies_df['duration'] = netflix_movies_df['duration'].str[0].astype(int)
netflix_movies_df.head()
```

</details>

### Director's movie

Sort the dataframe by director's name then by number of movie they've made in descending order  (don't forget that there are `NaN` values)

1. Sort by director's name:
<details><summary markdown='span'>Hint
</summary>

First you'll have to drop all director `NaN` values since we want to focus on directors and missing values are not needed. Check out the [`Dataframe.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) and its `subset` parameter.
</details>

<details><summary markdown='span'>View solution
</summary>

```python
netflix_movies_df.dropna(inplace=True, subset=["director"])
netflix_movies_df['director'].sort_values()
```
</details>

2. Sort by number of movie:
Here you have to use (like in covid exercise) [`DataFrame.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) but you don't want to `sum` the result

[`Dataframe.count()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html) is what you should use. Then you'll just have to use sort in descending order on the result

<details><summary markdown='span'>View solution
</summary>

```python
netflix_movies_by_director = netflix_movies_df.groupby(netflix_movies_df["director"]).count()['title']
netflix_movies_by_director = netflix_movies_by_director.sort_values(ascending=False)
netflix_movies_by_director
```
</details>

Plot the number of movies for the first 10 directors
<details><summary markdown='span'>View solution
</summary>

```python
plot = netflix_movies_by_director.head(10).plot(kind='bar')
plot
```

</details>

## Netflix American Comedy

Create a new dataframe that lists all American (US) shows (TV shows and movies) that are listed as Comedies. Pay attention, shows that have comedies AND another category should also be listed in this new dataframe.

You have to check if the 'listed_in' string contains 'Comedies'

<details><summary markdown='span'>View solution
</summary>

```python
conditions = np.logical_and(netflix_df["country"] == "United States", netflix_df["listed_in"].str.contains('Comedies'))
american_netflix_comedies = netflix_df[conditions].copy()
american_netflix_comedies.head()
```

</details>

## Daniel Radcliffe or Emma Watson shows

Create a new dataframe with the shows in which Daniel Radcliffe or Emma Watson have played (don't modify the original dataframe).

<details><summary markdown='span'>View solution
</summary>

```python
netflix_cast_df = netflix_df.copy()
netflix_cast_df.dropna(inplace=True, subset=['cast'])
emma_daniel_conditions = np.logical_or(netflix_cast_df["cast"].str.contains('Emma Watson'), netflix_cast_df["cast"].str.contains('Daniel Radcliffe'))
daniel_or_emma_shows = netflix_cast_df[emma_daniel_conditions].copy()
daniel_or_emma_shows.head()
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
