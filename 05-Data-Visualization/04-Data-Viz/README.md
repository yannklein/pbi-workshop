# Data Visualization

Today we're going to concentrate ourselves on plotting beautiful and helpful graphs for every situation. We're going to work on data visualization.
`Python` offers a lot of different ways to plot a set of data thanks to `matplotlib`, `seaborn` and several other modules.

## Load data

We'll first work on the well known COVID-19 data set and try different approaches to represent various information on graphs.
To start create a new notebook by opening your shell then typing:

```bash
cd python-beginners/05-Data-Visualization/04-Data-Viz
```

Import the usual modules:

```python
%matplotlib inline
import numpy as np
import pandas as pd
```

And a new one:

```python
import matplotlib.pyplot as plt
```

`pyplot` will help us to handle many details on our graphs (legend, size, ...).
Now load the csv and convert it to a dataframe.

<details><summary markdown='span'>View solution
</summary>

```python
covid_df = pd.read_csv("covid_19_data.csv", ",")
covid_df
```
</details>

## Convert date object to datetime
Convert the date column into `datetime` (we already did it in COVID-19 exercise).

<details><summary markdown='span'>View solution
</summary>

```python
covid_df["Date"] = pd.to_datetime(covid_df["Date"], format = "%Y-%m-%d")
covid_df
```
</details>

## US analyses and plotting

For the first exercise we're going to work on American (US only) data to make different plots that will give relevant information on the disease.
Start by creating a new dataframe (without modifying the original) containing only rows with US as country.

<details><summary markdown='span'>View solution
</summary>

```python
us_covid = covid_df[covid_df["Country/Region"] == "US"][['Date', "Deaths", "Confirmed", "Recovered"]].copy()
```
</details>

### Sort and discard values
If you remember correctly, the covid data set contains only cumulative data, meaning that in our US dataframe, only the last row of each month is relevant for us.
Convert your date column into a month column then sort the values by the `Confirmed` column. Finally, discard the useless rows by keeping only the last row of each month.

To do so, use :
- [DataFrame.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)
- [DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)

<details><summary markdown='span'>View solution
</summary>

```python
us_covid = covid_df[covid_df["Country/Region"] == "US"][['Date', "Deaths", "Confirmed", "Recovered"]].copy()
us_covid.Date = us_covid.Date.dt.month
us_covid.sort_values(by=['Deaths'], inplace=True)
us_covid.drop_duplicates(['Date'], keep='last', inplace=True)
```
</details>

### Set date as index
For the rest of the exercise we will plot data based on the date (months). To make it easier we're going to set the date column as the dataframe index
To do so, use [DataFrame.set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)

<details><summary markdown='span'>View solution
</summary>

```python
us_covid.set_index('Date', inplace=True)
```
</details>

### Plotting
We're now going to see different ways to plot the same information. We will also spend much more time to put some details on our plot to make it more user friendly.

#### Basic plot
Plot the 3 following data in the same graph : `Deaths`, `Confirmed`, `Recovered`.

Don't forget to set a title to your plot!

<details><summary markdown='span'>View solution
</summary>

```python
us_covid.plot(title="US COVID analyse")
```
</details>

#### Double y axis
On our plot we can see that the maximum value of the `Deaths` column is by far smaller that the maximum value of the `Confirmed` column.

To make our data easier to read, create a new plot with the left y axis for the `Deaths` column and the right y axis for `Confirmed` and the `Recovery` columns.

Don't forget your title !

<details><summary markdown='span'>Hint
</summary>

If you don't find how to do it, take a look at the `secondary_y` parameter of [Dataframe.plot](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html)

</details>

<details><summary markdown='span'>View solution
</summary>

```python
us_covid.plot(secondary_y=['Confirmed', 'Recovered'], title="US COVID analyse")
```
</details>

Now make the same plot but replace the curves by bars.

<details><summary markdown='span'>View solution
</summary>

```python
us_covid.plot(secondary_y=['Confirmed', 'Recovered'], kind='bar', title="US COVID analyse")
```
</details>

#### Subplots
Create a new plot that will be divided into 3 plots, one for each column (`Deaths`, `Confirmed`, `Recovered`). If your plots are too small use the `figsize` parameter.

If you don't want the x axis to be in common for the 3 plots, put the `sharex` parameter to `False`.

Don't forget your title!

<details><summary markdown='span'>View solution
</summary>

```python
us_covid.plot(subplots=True, figsize=(6,6), sharex=False, title="US COVID analyse")
```
</details>

## World data plots

We're now going to work with a new dataframe to collect worldwide records and plot them. Copy the original dataframe into a new one.

As usual with our COVID-19 dataframe, we have to rework it (due to cumulative data) to keep only interesting data.

Modify the `Date` column by its month data then sort the values by `Deaths` and drop the duplicates (`Country/Region` and `Date`)

- [DataFrame.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)
- [DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_df = covid_df.copy()
monthly_covid_df.Date = monthly_covid_df.Date.dt.month
monthly_covid_df.sort_values(by=['Confirmed'], inplace=True)
monthly_covid_df.drop_duplicates(['Country/Region', 'Date'], keep='last', inplace=True)
```
</details>

### Worldwide plot

#### Worldwide pie plot

Make a pie plot of 5 unique countries where the number of deaths is the highest. Your data are already sorted (ascending) by number of deaths, you only have to drop the duplicates of each country and set the `Country/Region` column as index.  

Don't forget your title !

[DataFrame.plot.pie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.pie.html)
To keep only a dataframe with uniques countries:

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_country_df = monthly_covid_df.drop_duplicates(["Country/Region"], keep="last").copy()
monthly_covid_country_df.set_index("Country/Region", inplace=True)
```
</details>

To plot only the 5 countries where the number of deaths are the biggest:

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_country_df.tail(5).plot.pie(y="Deaths", figsize=(12,8))
```
</details>

#### Worldwide area plot

Make an area plot of our 3 columns (`Deaths`, `Confirmed`, `Recovered`) grouped by `Date` on the same graph!  

Don't forget your title!

- [DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
- [DataFrame.groupby.sum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.sum.html)
- [DataFrame.plot.area](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.area.html)

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_sum_df = monthly_covid_df.groupby(monthly_covid_df['Date']).sum()
monthly_covid_sum_df[["Confirmed", "Deaths", "Recovered"]].plot.area(title="Worldwide cases area")
```
</details>

#### Worldwide bar plot

Make a *stacked* bar plot of our 3 columns (`Deaths`, `Confirmed`, `Recovered`) grouped by `Date` on the same graph (you can reuse variable that you previously created)!
Don't forget your title!

[DataFrame.plot.bar](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html)

<details><summary markdown='span'>View solution
</summary>

```python
monthly_covid_sum_df[["Confirmed", "Deaths", "Recovered"]].plot.bar(stacked=True, title="Worldwide cases bar plot")
```
</details>

## Airbnb New York neighbourhood

We'll now briefly work on a new dataset to tackle 2 interesting plots. Let's load the AirBnB csv stocked in the data visualization file.

<details><summary markdown='span'>View solution
</summary>

```python
airbnb_df = pd.read_csv("AB_NYC_2019.csv")
airbnb_df
```
</details>

### Affordable dataframe

Modify the dataframe to only keep flats which prices are lower than 500$.

<details><summary markdown='span'>View solution
</summary>

```python
airbnb_df = airbnb_df[airbnb_df['price'] <= 500]
```
</details>

### Distribution of flat prices based on the Neighbourhood group

We're going to plot the distribution of flat prices based on the Neighbourhood group with a new plot function called violinplot.
To do so, first import the `seaborn` module (do that at the top of your notebook and run the first cell again).

```python
import seaborn as sns
```

Now read the documentation of [seaborn.violinplot](https://seaborn.pydata.org/generated/seaborn.violinplot.html) and use it to plot the distribution.

If your graph is too small use [plt.figure](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.figure.html) figsize parameter!

Don't forget your title (use `plt.title`)!

<details><summary markdown='span'>Hint
</summary>

The `data` parameter will take your dataframe
the `x` and `y` parameter should respectively take `neighbourhood_group` and `price`..
</details>

<details><summary markdown='span'>View solution
</summary>

```python
sns.violinplot(data=airbnb_df, x="neighbourhood_group", y="price", title="distribution ")
```
</details>

<details><summary markdown='span'>View solution
</summary>

```python
plt.figure(figsize=(15,8))
plt.title("Distribution of flat prices based on the Neighbourhood group")
sns.violinplot(data=airbnb_df, x="neighbourhood_group", y="price")
```
</details>

### Plot the AirBnB localisation on a map

#### scatter plot

This dataframe is well made because you can see that each AirBnB has its geographic coordinates. We'll use them to create a scatter plot and put each AirBnB on a New York City map.

To do so you'll use [DataFrame.plot.scatter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html).

You'll have to give as `x` the `longitude` and as `y` the `latitude`.
The `c` parameter allows you to put a different color to each point.
The `s` parameter allows you to make your points have a variable size based on their price.

Put also those 3 parameters in your scatter methods:
```python
figsize=(20,12), colorbar=True, cmap="inferno"
```

<details><summary markdown='span'>View solution
</summary>

```python
airbnb_df.plot.scatter(x="longitude", y="latitude", c = "price", s=airbnb_df["price"]*0.02, figsize=(20,12), colorbar=True, cmap="inferno")
```
</details>

#### Add map to the background
We're going to add to the background the New York city image stored in our data vizualisation file.

Pyplot has two functions to help you read and load images into graphs. You'll first have to use [`plt.imread`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imread.html) and then [`plt.imshow`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) with as first parameter the loaded image.

To make your scatter points fit with the map you also need to fill the extent paramater in with a list containing the minimal and maximal value of the `longitude` and `latitude` column.

Now reuse the previous scatter function but add the ax parameter with [plt.gca](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.gca.html) to merge it with the image:

```python
ax = plt.gca()
airbnb_df.plot.scatter(ax=ax)
```

<details><summary markdown='span'>View solution
</summary>

```python
im = plt.imread(r"Neighbourhoods_New_York_City_Map.png")
ext = (airbnb_df.longitude.min(), airbnb_df.longitude.max(), airbnb_df.latitude.min(), airbnb_df.latitude.max())
lim = (-74.258, -73.7, 40.49, 40.92)
plt.imshow(im, zorder=0, extent = ext)
ax = plt.gca()
airbnb_df.plot(kind="scatter", ax=ax, zorder=1, x="longitude", y="latitude", c = "price", s=airbnb_df["price"]*0.2, alpha=0.8, figsize=(20,12), colorbar=True, cmap="inferno")
```
</details>

## Pushing your code to GitHub

Remember the steps we did in the first two days to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `Exercise.ipynb` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Complete my first Data Analysis with Jupyter Notebook`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window
