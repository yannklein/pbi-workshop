# Project - Youtube's Statistics

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

YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes). Note that they’re not the most-viewed videos overall for the calendar year”. Top performers on the YouTube trending list are music videos (such as the famous “Gangam Style”), celebrity and/or reality TV performances, and the random dude-with-a-camera viral videos that YouTube is well-known for.

The dataset stored in *USvideos.csv* is a daily record of the top trending YouTube videos in the United States.

* `video_id` Contains the id of the youtube videos
* `trending_date` Contains the trend date of the youtube videos
* `title` Contains the title of the youtube videos
* `channel_title` Contains the name of the channel the youtube videos belong to
* `category_id` Id of the category, the youtube videos belong to
* `publish_time` Contains the time of publication of the youtube videos
* `tags` Contains the tags associated to the youtube videos
* `# views` Contains the number of views of the youtube videos
* `# likes` Contains the number of likes of the youtube videos
* `# dislikes` Contains the number of dislikes of the youtube videos
* `# comment_count` Contains the number of comments of the youtube videos
* `thumbnail_link` Contains the link to the images associated with the youtube videos
* `comments_disabled` Whether the comments are disabled or not
* `ratings_disabled` Whether the ratings are disabled or not
* `video_error_or_removed` Whether the video is unreachable or not
* `description` Contains the textual descriptions of the youtube videos

## Enriching Data

:warning: Not all proposed external Data sources are just pluggable or needed, you may have to get inventive to use them (if you use any). Especially since some constraints may be associated with the Data sources (i.e. number of calls limited for an API by key).
Take a quick look and sort out which sources are interesting or not too time consuming for your approach then generate keys if needed.

**External File**

* *US_category_id.json* contains data related to the `category_id` used the base dataset.

**Scraping**

* [Most-subscribed Youtube channels](https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels)

## Some Leads

* Analysing what factors affect how popular a YouTube video will be
* Statistical analysis over time
* Categorising YouTube videos based on their comments and statistics
* Sorting most popular channels

**Modules**

* [WordCloud](https://pypi.org/project/wordcloud/)
