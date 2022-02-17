# Project - Bangalore's Restaurants

The goal of this project is to simulate real conditions of data analysis. Starting from an original dataset, your objective will be to find an approach allowing you to obtain relevant observations on these data. The whole thing will be done in teams, so be careful to coordinate well and to all have the same understanding of the final objective.

If the data inspires you moderately, don't worry, we will provide some initial questions and food for thoughts. But nothing prevents you from bringing your own touch by going beyond the initial canvas: by highlighting points that differ from those proposed or by completing the data with sources that we had not provided.

The approach will stick to what you learned during this week, do not forget that the lines you coded may still be useful on later projects :wink:

The steps:

* Data loading
* Data exploration
* Data cleaning
* Data enrichment
* Data analysis
* Data visualization

Obviously some tasks may be way quicker than others and you're a group, don't get scared!

At the end of the day, we're expecting a quick overview of your notebook: how did you decide to analyze the data, what was your approach, which interesting facts did you retrieve from you analysis and how did you show them? The goal is not to have everything prepared perfectly and finished neatly. But to see how far you got, what caught your attention and how you cooperated.

## Initial Data

The food culture of Bengaluru is pretty rich. Restaurants from all over the world can be found in Bengaluru. From United States to Japan, Russia to Antarctica, you get all type of cuisines there. Delivery, Dine-out, Pubs, Bars, Drinks, Buffet, Desserts you name it and Bengaluru has it. Bengaluru is the best place for foodies. The number of restaurants is increasing day by day. And yet this industry hasn't been saturated yet, new restaurants are opening every day. However it has become difficult for them to compete with already established ones.

You can find the dataset by clicking on this [link](https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants/download). Information were scraped from the [Zomato](https://www.zomato.com/bangalore) website on 15-03-2019. Each line of the dataset *zomato.csv* consists in a restaurant present in the area and information about the demographics of its location.

* `url` Contains the url of the restaurant in the zomato website
* `address` Contains the address of the restaurant in Bengaluru
* `name` Contains the name of the restaurant
* `online_order` Whether online ordering is available in the restaurant or not
* `book_table` Table book option available or not
* `rate` Contains the overall rating of the restaurant out of 5
* `# votes` Contains total number of rating for the restaurant as of the date of the scraping
* `phone` Contains the phone number of the restaurant
* `location` Contains the neighborhood in which the restaurant is located
* `rest_type` Restaurant type
* `dish_liked` Dishes people liked in the restaurant
* `cuisines` Food styles, separated by comma
* `approx_cost(for two people)` Contains the approximate cost for meal for two people
* `reviews_list` List of tuples containing reviews for the restaurant, each tuple consists of two values, rating and review by the customer
* `menu_item` Contains list of menus available in the restaurant
* `listed_in(type)` Type of meal
* `listed_in(city)` Contains the neighborhood in which the restaurant is listed

## Enriching Data

:warning: Not all proposed external Data sources are just pluggable or needed, you may have to get inventive to use them (if you use any). Especially since some constraints may be associated with the Data sources (i.e. number of calls limited for an API by key).
Take a quick look and sort out which sources are interesting or not too time consuming for your approach then generate keys if needed.

**External File**

* *franchises.csv* contains data related to the 250 biggest restaurant franchises. This file was downloaded form the [restaurantbusinessonline website](https://www.restaurantbusinessonline.com/).

**APIs**

* [Exchange Rates API](https://exchangeratesapi.io/)
* [Zip·po·pot·amus](http://www.zippopotam.us/#where)
* [Position Stack](https://positionstack.com/documentation)
* [Open Cage Data](https://opencagedata.com/)

**Scraping**

* [Culinary top 10](https://edition.cnn.com/travel/article/world-best-food-cultures/index.html)
* [Bangalore's neighborhoods](https://en.wikipedia.org/wiki/List_of_neighbourhoods_in_Bangalore)

## Some Leads

* Location of the restaurants (on a map?)
* Approximative price of food
* Theme based / franchised restaurants or not
* Which locality of that city serves that cuisines with maximum number of restaurants
* The needs of people who are striving to get the best cuisine of the neighborhood
* Is a particular neighborhood famous for its own kind of food.

**Modules**

* [Geopy](https://geopy.readthedocs.io/en/stable/)
* [Folium](https://pypi.org/project/folium/0.1.5/)
* [WordCloud](https://pypi.org/project/wordcloud/)
