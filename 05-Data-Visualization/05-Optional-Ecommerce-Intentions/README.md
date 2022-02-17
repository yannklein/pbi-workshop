# Data Visualization

Today we're going to concentrate ourselves on plotting beautiful and helpful graphs for every situation. We're going to work on data visualization.
`Python` offers a lot of different ways to plot a set of data thanks to `matplotlib`, `seaborn` and several other modules.

## Load data

We'll now work on a data set containing online shoppers' intentions and try different approaches to represent various information on graphs.
To start create a new notebook by opening your shell then typing:

```bash
cd python-beginners/05-Data-Visualization/05-Optional-Ecommerce-Intentions
```

Import the usual modules:

```python
import numpy as np
import pandas as pd
```

And a few new ones:

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

Now load the csv and convert it to a dataframe.

<details><summary markdown='span'>View solution</summary>

```python
ecommerce_df = pd.read_csv("online_shoppers_intention.csv")
ecommerce_df
```
</details>

### Dataset Attributes

Each line of the dataset consists in a session of an user on the website. The [`Bounce Rate`](https://www.hotjar.com/google-analytics/glossary/bounces/), [`Exit Rate`](https://www.hotjar.com/google-analytics/glossary/exits/) and [`Page Value`](https://yoast.com/what-is-page-value-in-google-analytics/) features represent the metrics measured by "Google Analytics" for each page in the e-commerce site.

* **Administrative, Administrative Duration, Informational, Informational Duration, Product Related and Product Related Duration** => Represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.
* **Bounce Rate** => Percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics server during that session.
* **Exit Rate** => Percentage that were the last in the session
* **Page Value** => Represents the average value for a web page that a user visited before completing an e-commerce transaction.
* **Special Day** => indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with transaction. For example, for Valentina’s day, this value takes a nonzero value between February 10 and February 18, zero,before and after this date unless it is close to another special day, and its maximum value of 1 on February 14. The closer the visit gets from the bounds to the special day the greater the value between 0 and 1 (e.g. The value is set to 0.4 on February 11).
* **Month** => Month of the year.
* **Operating System, Browser, Region, Traffic Type** => Different types of operating systems, browser, region and traffic type used to visit the website.
* **Visitor Type** => Whether the customer is a returning or new visitor.
* **Weekend** => A Boolean value indicating whether the date of the visit is weekend.
* **Revenue** => Class whether the session can make a revenue or not

## Univariate Analysis

The first thing we're interested in is obviously the number of sessions resulting in a source of revenue. Plotting this information will allow us to observe that most of the visits in e-commerces are not generating incomes. Which means that we provide resources to reach a large audience in which only a few will respond to the appeal of buying.
Plot the number of sessions generating revenue and the ones that are not with [countplot()](https://seaborn.pydata.org/generated/seaborn.countplot.html).

<details><summary markdown='span'>
View solution
</summary>

```python
plt.title('Number of Sessions Generating Revenue')
sns.countplot(data=ecommerce_df, x='Revenue')
```
</details>

You can now generate a new DataFrame `revenue_df` containing only the sessions generating revenue. Based on this DataFrame, does being in weekend have a significant impact or not?

<details><summary markdown='span'>
Hint
</summary>

What is the type of the `Revenue` column?
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
revenue_df = ecommerce_df[ecommerce_df['Revenue']]
sns.countplot(data=revenue_df, x='Weekend')
```

The propensity to purchase seems to remain the same.
</details>

How could you use a second category in `countplot()` to not have to generate the DataFrame and simply use `ecommerce_df`?

<details><summary markdown='span'>
Hint
</summary>

Check the [countplot()](https://seaborn.pydata.org/generated/seaborn.countplot.html) documentation for some extra parameters.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
sns.countplot(data=ecommerce_df, x='Weekend', hue='Revenue')
```

</details>

### Subplots
This type of analysis can also be done on plenty of other categorical values: `Month`, `Region`, `OperatingSystems`, `Browser`, `TrafficType` and even `VisitorType`.

Use the [plt.figure()](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html) function to create a new plot that will be divided into 6 plots (7 with `Weekend`) allocated with [plt.subplot()](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.subplot.html), one for each column we will compare with `Revenue`. If your plots are too small use the `figsize` parameter.

If you don't want the y axis to be in common for the plots, put the `sharex` parameter to `False`.

Don't forget your titleS!

<details><summary markdown='span'>
Hint
</summary>
If you're bored, you can create a loop to display all those plots quite easily. Only a few will be interesting but it grants you a quick overview and tell where to look.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
columns=['OperatingSystems', 'Browser', 'Region', 'TrafficType', 'Month', 'VisitorType', 'Weekend']    
plt.figure(figsize=(30, 30))
plot_number = 0
for col in columns:
    plot_number = plot_number + 1
    ax = plt.subplot(6, 2, plot_number,adjustable='datalim')
    sns.countplot(data=ecommerce_df, x=col, hue='Revenue')
    ax.set_title('Customers adding Revenue based on '+ col)
    plt.tight_layout()
```

</details>

### Consultation Peaks

By using the `Month` column you'll also be able to discern the peaks of activity on the website. What kind of plot should you use? Compare the results with the peaks where the commerce was generating most revenues. How can you add a second category?

<details><summary markdown='span'>
Hint
</summary>

While a barchart would simply do, the main interest is to have the distribution of an unique type of values. In this case the [histplot()](https://seaborn.pydata.org/generated/seaborn.histplot.html) is the best choice.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
sns.histplot(data=ecommerce_df, x='Month')
sns.histplot(data=revenue_df, x='Month')
```

Or even better

```python
sns.histplot(data=ecommerce_df, x='Month', hue='Revenue')
```

</details>

<details><summary markdown='span'>
Observations
</summary>

We can observe an increase in the number of positive `Revenue` in November, December and May. For the first two, we may assume it is related to the end of the year festivities and gifts.
May is a bit harder to associate but it may be related to Mother's Day and Father's Day.

We can also observe that after each peaks we have a decrease in the number of sessions in the following months.
</details>

## Relations between Attributes
We would now like to identify the attributes influencing the `Revenue`and the relations in between attributes. The first we'll check are `SpecialDay`, `ProductRelated` and `ProductRelated_Duration`. How can you check their correlation by observing a [pairplot()](https://seaborn.pydata.org/generated/seaborn.pairplot.html)?

<details><summary markdown='span'>
Hint
</summary>

Instead of computing the pairplot for all possible combinations of the dataframe, checkout the `x_vars` and `y_vars` parameters.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
sns.pairplot(data=ecommerce_df, hue='Revenue',
    x_vars=["SpecialDay", "ProductRelated", "ProductRelated_Duration"],
    y_vars=["SpecialDay", "ProductRelated", "ProductRelated_Duration"])

```
</details>

<details><summary markdown='span'>
Observations
</summary>

Contrary to what one might think, `productRelated` and `productRelatedDuration` does not seem correlated with `SpecialDay` as we can see most of the visits are when the value is equal to 0.
We suppose that the users usually visit the websites several days before `SpecialDaly` like Christmas and use to spend more time with their family during these special days.

On the other hand, `ProductRelated` and `ProductRelatedDuration` are well positive correlated as expected. Indeed, the more pages you visit, the more time you spend.
</details>


### Comparing Google Analytics Data

Statistical analysis is a process of understanding how variables in a dataset relate to each other and how those relationships depend on other variables. Visualization can be a core component of this process because, when data are visualized properly, the human visual system can see trends and patterns that indicate a relationship. Our first goal will be to identify the relation between `BounceRates` and `ExitRates` thanks to [relplot()](https://seaborn.pydata.org/generated/seaborn.relplot.html).

<details><summary markdown='span'>
Hint
</summary>

`False` `Revenue` values may cover the `True` ones, use the `col` parameter to discern all you data.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
sns.relplot(x="BounceRates", y="ExitRates", col="Revenue", hue="Revenue", data=ecommerce_df)

```
</details>

<details><summary markdown='span'>
Observations
</summary>

We can see that high `Bounce` and `Exit Rates` lead to no `Revenue`.

If we add `Weekend` data as `type` parameter, we can also see that the rates increase when it is not a weekend. Which may be related to the fact that people have less time to spend doing window shopping.
</details>

### Impact of Durations
The last observation led us to wonder if the amount of time spent on the website during a session could have an impact on the generation of `Revenue`. Use [catplot()](https://seaborn.pydata.org/generated/seaborn.catplot.html) to determine if it's the case.

<details><summary markdown='span'>
Hint
</summary>

We ca either use `catplot()` on all duration columns or sum all the columns in a new one before using it.
</details>

<details><summary markdown='span'>
View solution
</summary>

```python
for col in ecommerce_df.columns:
    if 'Duration' in column:
        sns.catplot(data=ecommerce_df, y=col, x='Revenue')

```
</details>

<details><summary markdown='span'>
Observations
</summary>
We can see that most people purchase something when they don't spend too long on the website. The longer the customer spend on the website the less likely he becomes to buy.
</details>

### Exit Rates by User Type
We would also like to analyze the `ExitRates` by type of visitors. Use [catplot()](https://seaborn.pydata.org/generated/seaborn.catplot.html) to visualize data with one numerical attribute and one categorical attribute. Obviously you can still add extra categories thanks to the parameters (such as `Revenue` and `Weekend`).

<details><summary markdown='span'>
View solution
</summary>

```python
sns.catplot(x="VisitorType", y="ExitRates",
                hue="Weekend", col="Revenue",
                data=ecommerce_df, kind="violin")

```
</details>

<details><summary markdown='span'>
Observations
</summary>

The exit rates are very lowly spread when there is a `Revenue` and there isn't much change in exit rates considering the `Weekend` and type of visitors.

A large variation can be seen in exit rates for the "other" category of visitors when it is in `Weekend` and there isn't any `Revenue` made. May be they are of casual window shopping kind.

New visitors have low exit rates and those are pretty much same in both revenue cases. They seem interested in exploring the website thoroughly. Which means we can't blame its attractiveness for its potential lack of popularity.
</details>

## Main Insights and Strategies

**Insights:**
* Lack of visits out of specific months
* For returning visitors the exit rates are high which show disinterest
* Website UI seems user friendly since new visitors have low exit rates
* Spending too much time on the website since to indicate an absence of revenu

**Strategies:**
* Introducing ad banners as special offers to prevent the customer to quit the page
* Engaging loyal customer with loyalty advantages
* Increase visits on monthly basis by introducing monthly themed offers and products. Could also increase conversion rate
* Shorten the number of access to make to reach the page ensuring a revenue

## Pushing your code to GitHub

Remember the steps we did in the first two days to save the code on GitHub? Let's do it again, for this new exercise:

1. Open GitHub Desktop
1. It should automatically detect that the `Exercise.ipynb` file has changed. If not, ask a TA
1. Make sure this file is ticked, and write a _commit message_ in the bottom left form (For instance: `Complete my first Data Analysis with Jupyter Notebook`)
1. Click on the "Commit to `master`" button at the bottom of the form
1. Click on the "Push `origin`" button at the top of the window
