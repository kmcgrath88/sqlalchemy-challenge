#  Honolulu, Hawaii Vacation

Thanks for checking out my project's repo! You can view a Honolulu, Hawaii climate analysis through my jupyter notebook file. Also, by downloading my repo and running app.py through flask, you can view additional climate information through available API routes. <br>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Project Instructions](#project-instructions)

<!--About the Project-->
## About the Project

<b>The Jupyter notebook Honolulu, Hawaii climate analysis includes: </b>
* Precipitation analyses and visualizations
* Station analyses and visualizations
* Temperature analyses, visualizations, and predictions

<b>Available routes through Flask API: </b><br>

/api/v1.0/precipitation <br>

/api/v1.0/stations <br>

/api/v1.0/tobs <br>

/api/v1.0/start_date <br>
Example: /api/v1.0/2016-03-10 <br>

/api/v1.0/start_date/end_date <br>
Example: /api/v1.0/2016-03-10/2016-03-20 <br>

<!--Built With-->
### Built With
This project was built using the following frameworks/libraries/databases:<br>
* Python
* SQLAlchemy
* Flask
* Pandas
* Matplotlib
* NumPy
* SciPy
* Datetime
* SQLite

<!--Project Instructions-->
## Project Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.<br>

### Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.<br>
-Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.<br>
-Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.<br>
-Use SQLAlchemy create_engine to connect to your sqlite database.<br>
-Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.<br>

#### Precipitation Analysis
-Design a query to retrieve the last 12 months of precipitation data.<br>
-Select only the date and prcp values.<br>
-Load the query results into a Pandas DataFrame and set the index to the date column.<br>
-Sort the DataFrame values by date.<br>
-Plot the results using the DataFrame plot method.<br>
-Use Pandas to print the summary statistics for the precipitation data.<br>

#### Analysis
-Design a query to calculate the total number of stations.<br>
-Design a query to find the most active stations.<br>
-List the stations and observation counts in descending order.<br>
-Which station has the highest number of observations?<br>
-Design a query to retrieve the last 12 months of temperature observation data (TOBS).<br>
-Filter by the station with the highest number of observations.<br>
-Plot the results as a histogram with bins=12.<br>

### Step 2 - Climate App
-Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed. Use Flask to create your routes.<br>

-Routes:<br>
/
Home page.<br>
List all routes that are available.<br>
<br>
/api/v1.0/precipitation<br>
Convert the query results to a dictionary using date as the key and prcp as the value.<br>
Return the JSON representation of your dictionary.<br>
<br>
/api/v1.0/stations<br>
Return a JSON list of stations from the dataset.<br>
<br>
/api/v1.0/tobs<br>
Query the dates and temperature observations of the most active station for the last year of data.<br>
Return a JSON list of temperature observations (TOBS) for the previous year.<br>
<br>
/api/v1.0/start_date and /api/v1.0/start_date/end_date<br>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br>
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.<br>
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.<br>

### Bonus: Other Recommended Analyses

The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.<br>

#### Temperature Analysis I

Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?<br>
You may either use SQLAlchemy or pandas's read_csv() to perform this portion.<br>
-Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.<br>
-Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?<br>

#### Temperature Analysis II

The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.<br>
-Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").<br>
-Plot the min, avg, and max temperature from your previous query as a bar chart.<br>
-Use the average temperature as the bar height.<br>
-Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).<br>

#### Daily Rainfall Average

-Calculate the rainfall per weather station using the previous year's matching dates.<br>
-Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.<br>
-You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.<br>
-Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.<br>
-Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.<br>
-Use Pandas to plot an area plot (stacked=False) for the daily normals.