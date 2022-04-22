# surfs_up
A project based on SQLite, SQLAlchemy, and Flask to build on our knowledge of SQL database structures and querying methods. Python code in a Jupyter notebook and create graphs using Python.

## Background
We are doing weather analysis to determine if the surf and ice cream shop business is sustainable year-round on the islands of Hawaii.For that we have to analyze and determine the Summary Statistics for June and also for December and write a report for the statistical analysis.

### Determine the Summary Statistics for June :

Using Python, Pandas functions and methods, and SQLAlchemy, we filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. Then converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics.For this we wrote a query that filters the date column from the Measurement table to retrieve all the temperatures for the month of June.Then converted the June temperatures to a list.Created a DataFrame from the list of temperatures for the month of June.And then generated the summary statistics for the June temperatures DataFrame as shown below: 

- The summary statistics for the June temperatures :

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/june_temp_analysis.png)

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/june_temp_plot.png)

### Determine the Summary Statistics for December :

Using Python, Pandas functions and methods, and SQLAlchemy, we filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December,then converted those temperatures to a list,created a DataFrame from the list, and generated the summary statistics.For that, we wrote a query that filters the date column from the Measurement table to retrieve all the temperatures for the month of December.Then converted the December temperatures to a list.Created a DataFrame from the list of temperatures for the month of December. In the end,generated the summary statistics for the December temperatures DataFrame as below :

The summary statistics for the December temperatures DataFrame

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/december_temp_analysis.png)

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/december_temp_plot.png)

The key differences in weather between June and December and two recommendations for further analysis.
- We see that on average the recorded temperature was higher in June than December.
- We also find there is a larger spread in the December data as shown by its increased standard deviation, indicating there are likley some December days with temperatures reaching those of June. This is also confirmed by the roughly equal maximum temperatures for each month.

- The summary statistics for the June and December Precipitation Analysis :
Considering additional weather data, we can compare levels of precipitation between the two months using the query:and similarly for December. Doing so shows there are increased levels of precipitation in December, but again with greater variation in the measured data.
 
![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/june_prcp_analysis.png)

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/june_prcp_plot.png)

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/december_prcp_analysis.png)

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/december_prcp_plot.png)

From the above graphs we can say that with good temperatures and less precipitation, June is a good month for the business on the island of Oahu.

For further analysis, we combined both the datasets into one to find out the name of the islands with weather stations. The combines table looks like below: 

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/measurement_station.png)

From this data, we wrote two functions to get temprature and precipitation from last year to Calculate the rainfall per weather station and temperature for our trip dates using the previous year's matching dates.

![alt_text](https://github.com/RGK73/surfs_up/blob/main/Images/querries.png)
