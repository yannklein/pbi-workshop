Using Python and Pandas does not mean we do not use Excel. On the contrary!

Let's dive into [XLWings](https://www.xlwings.org/)

## Setup

XLWings is part of Anaconda. Otherwise it can be easily [downloaded with `conda`](https://docs.xlwings.org/en/stable/installation.html#).

One important part is to install the [**add-in** for Excel](https://docs.xlwings.org/en/stable/addin.html). The easiest way is to open the Anaconda Prompt and run:

```bash
xlwings addin install
xlwings runpython install
```

## Documentation

After setting up XLWings, read some important parts:

- [Syntax Overview](https://docs.xlwings.org/en/stable/syntax_overview.html)
- [Data Structures Tutorial](https://docs.xlwings.org/en/stable/datastructures.html)

## From Notebook to Excel

You can load data from your Notebook into Excel [like specified in the doc](https://docs.xlwings.org/en/stable/datastructures.html#pandas-dataframes).

Let's take this morning's exercise on the IMDB Scraping and load the data from our Pandas Dataframe into Excel.

To use the **active spreadsheet**, you can directly use:

```python
import xlwings as xw

xw.Range('A1').value = movies_df
```

## Macros

Let's see how we can call Python code directly from Excel thanks to the [`RunPython`](https://docs.xlwings.org/en/stable/vba.html) module. That way we can build a **UI** (User Interface) with it!

```bash
cd $SOME_PATH
xlwings quickstart livecode
```

Let's re-use this morning's livecode with the MetaWeather API and replace the `input()` with Excel controls.

```python
import requests

city = input("Which city?\n> ")
url = f"https://www.metaweather.com/api/location/search/?query={city}"

response = requests.get(url)
data = response.json()
woeid = data[0]['woeid']

url = f"https://www.metaweather.com/api/location/{woeid}/"
response = requests.get(url)
data = response.json()

for day in data['consolidated_weather']:
    weather = day['weather_state_name']
    date = day['applicable_date']
    temp = round(day['max_temp'], 1)
    print(f"- {date}: {weather} ({temp} C)")
```
