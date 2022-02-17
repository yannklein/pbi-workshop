# Storing notebooks

Let's practise git & GitHub by creating a repository `notebooks` on your public GitHub account.

## Create the repo on GitHub

Make sure you are logged in to GitHub and go to [github.com/new](https://github.com/new). Fill the form with the following information:

- Repository name: `notebooks`
- Description: `Collection of my personal experimental notebooks`
- Choose `Public` or `Private` (GitHub is [now free](https://github.com/pricing) for private repos)
- Tick the checkbox `Initialize this repository ...`
- Add a .gitignore => choose `Python` in the dropdown menu
- Add a license => leave it to `None`

Finally, click on the big green button "Create repository".

## `Cloning` to the computer

Open **GitHub Desktop** on your computer and **clone** this newly created project to your hard drive. Open Anaconda Prompt and navigate to that folder. Then:

```bash
jupyter notebook
```

Create a new notebook, name it `Lab`, and add a few cells:


# Lab

This notebook serves for quick experimentation.

Before we can get any data from this API you will need to get your PUBLIC_API_KEY from [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens), and then copy/paste it in the public_api_key variable.


```python
import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib
import requests
```

```python
stocks = ["goog", "aapl", "fb", "amzn"]
public_api_key = "COPY_PASTE_HERE_YOUR_PUBLIC_API_KEY"

stocks_df = None
for stock in stocks:
    data = requests.get(f"https://cloud.iexapis.com/stable/stock/{stock}/chart/3m?token={public_api_key}").json()
    stock_df = pd.DataFrame.from_dict(data)
    stock_df['date'] = pd.to_datetime(stock_df['date'], format="%Y-%m-%d")
    stock_df = stock_df.set_index('date')
    stock_df = stock_df[["close"]]
    stock_df.columns = [ stock ]
    stock_df = stock_df / stock_df[stock][0] # Normalization at t=0
    if stocks_df is None:
        stocks_df = stock_df
    else:
        stocks_df = stocks_df.join(stock_df)

stocks_df.plot(figsize=(12,8))
```

## `commit` and Push

Go back to **GitHub Desktop** and do your first commit. Remember it's a two-step process, first you need to select the files you want to put in the commit, then write the commit message and click on the button.

Then **push** your commit to GitHub

## Checking it's been pushed on GitHub

Go to [github.com](https://github.com) and go to your `notebook` repository. Check that the notebook `Lab.ipynb` is there. Click on it, it loads for a few seconds and them, :tada: you can see your notebook online! It's not interactive, but you can share the URL with a colleague so they can quickly get an idea of your data analysis. If they are interested they can even **fork** your repository and clone it to their computer to take it from there and continue the exploration!

---

## A word about GitHub Enterprise

Your company might be using [GitHub Enterprise](https://github.com/enterprise) which is an on-premise version of the GitHub website we used this week. Know that all the commands, all the software, all of it works _exactly the same_ there!
