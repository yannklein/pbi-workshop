# News API
In this exercise we're going to learn how to read and use API documentation to get some data and be able to work with it.
We're going to use a [news](https://newsapi.org/docs) API that contains news data from different sources around the world.

## Subject of your choice
You're going to choose a subject and get datas from the [news](https://newsapi.org/docs) about it.

### API setup

An API is often protected by a personal key that you have to keep secret but for this exercise we provide you with test API keys for you to use _only during the challenge today_. We trust you! Pick the one corresponding to the first letter of your name :wink:

Here it is:

```bash
A-E: 23be86fd871a4461b0b49177e5952954
F-J: 4915859c995c4cefa0743d2bd8003dce
K-O: 4b41f229044844119a4c7ab953130a1e
P-T: 8171b0b3bb474fcba2ba641da7d329a9
U-Z: 11d5e42021054000a85e928901e4d909
```

You can try it in your browser like [this](http://newsapi.org/v2/top-headlines?apiKey=23be86fd871a4461b0b49177e5952954&country=fr). Take the time to checkout the url.

### Using the API

Let's find in the news API the **URL** corresponding to the **top headlines** in the **category of your choice**! If you don't know what to choose, take the category `general`. You can also choose from which country information should come.

⚠️ Take your time before reading the solution, finding what we want in API documentations can usually take **10 to 15 minutes of reading**

<details><summary markdown='span'>View Solution
</summary>
You can find all information and parameters that you need in this documentation:
<a href="https://newsapi.org/docs/endpoints/everything">https://newsapi.org/docs/endpoints/everything</a>

The URL is:
<pre>
http://newsapi.org/v2/top-headlines?apiKey=23be86fd871a4461b0b49177e5952954&country=us&category=general
</pre>
</details>

## Using API data in pandas

### Setup
For this exercise we will work in a Notebook.

```sh
jupyter notebook
```
Go ahead and create a new Python Notebook in the `04-Data-Sourcing/news-api` folder of your python-challenges repository.

Start with the usual imports in the first cell:

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib
```
We will reuse the **API URL** for the **news of the whole month about your subject** here.

To make a **call** to the API you can use the following code:

```python
import requests

url = "YOUR_API_URL"
api_data = requests.get(url).json()
```

You can now **create a dataframe** from this data. Pay attention, in our `Dataframe` we only need the data stored in the `articles` key.

<details><summary markdown='span'>View Solution
</summary>

```python
news_df = pd.DataFrame.from_dict(api_data['articles'])
news_df.head()
```
</details>

### Convert publication date to datetime

To do that you can use Pandas.to_datetime()

- **pd.to_datetime** documentation: [http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
- **Format** documentation: [http://strftime.org/](http://strftime.org/)

### Get name from source column

As you can see, the source column contains a dictionary with two keys: id and name. rewrite the source column and put only the name of the sources.

<details><summary markdown='span'>Hint
</summary>
[`.str.get()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get.html) function also works with dictionaries. :wink:
</details>

<details><summary markdown='span'>View Solution
</summary>

```python
news_df['source'] = news_df['source'].str.get("name")
news_df.head()
```
</details>

### Sort the news by publication hour

You'll be able to sort the articles to get the most recent ones. The same function can be used with other parameters to get the oldest ones first.

<details><summary markdown='span'>View Solution
</summary>

```python
news_df.sort_values(by=['publishedAt']).head()
```
</details>

### Plot the number of articles for each source (ascending)

Remember, to do so you'll have to use:

- **df.groupby** documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pd.groupby)
- **df.groupby.count()** documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.count.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.count.html)

<details><summary markdown='span'>View Solution
</summary>

```python
news_per_source_df = news_df.groupby(news_df["source"])["title"].count()
news_per_source_df.sort_values(inplace=True)
plot = news_per_source_df.plot(kind="bar")
plot
```
</details>

### Find all article containing a word of your choice
Try to find a word that some article content may contain and to filter you dataframe to get only those article.

<details><summary markdown='span'>View Solution
</summary>

```python
news_df.dropna(inplace=True, subset=['content'])
news_specific_df = news_df[news_df["content"].str.contains("YOUR-WORD")].copy()
news_specific_df.head()
```
</details>

## Back to the API

Let's find out what kind of data we can get from this API 🕵️‍♂️

### What is the URL for:

1. all top-headlines from your native language containing the translation of "President"
2. all news in english since 10 days about "Trump"
3. all sports american sources
4. all english articles whose title contains "US" sorted by popularity

<details><summary markdown='span'>All Solutions
</summary>
        - https://newsapi.org/v2/top-headlines?country=fr&apiKey=23be86fd871a4461b0b49177e5952954&q=Pr%C3%A9sident
        - https://newsapi.org/v2/everything?q=Trump&from=2020-09-28&to=2020-10-04&apiKey=23be86fd871a4461b0b49177e5952954&language=en
        For articles in the week of the 28-09-2020.
        - https://newsapi.org/v2/sources?apiKey=23be86fd871a4461b0b49177e5952954&country=us&category=sports
        - https://newsapi.org/v2/everything?qInTitle=US&apiKey=23be86fd871a4461b0b49177e5952954&sortBy=popularity

</details>
