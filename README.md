# MLDataCollection
Repository for data collection used in Machine Learning Course at UPC in spring semester 2017

# Description
As machine learning project in the spring semester at UPC we need to implement a project and write a report about it. 
The basis for our project: https://github.com/limcheekin/r-flight-delay-prediction

We want to improve the existing project with weather data, similar to what is described in this paper:
http://ieeexplore.ieee.org/document/7777956/?reload=true

The data for the delay of the airplanes we get from here:
https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time

This python script is intendet to enrich the data about delayed planes by weather data which we want to collect from here:
https://developer.worldweatheronline.com/api/historical-weather-api.aspx (If they give us more then 500 api calls per day ;))

If you want to use it you need to add a file "weatherAPI.key" in the data folder with your API-key from worldweatheronline.

In data you find the original data from bts, the full dataset as well as one with one line and 20 lines for test purposes.

Output is generated in data folder named raw_with_weather.csv. 

Here you should see the following additional fields:

TEMPC,
HUMIDITY,
WINDSPEEDKMH,
WINDDIRDEGREE,
WEATHERCODE,
VISIBILITY,
CLOUDCOVER,
PRESSURE

Description over the fields can be found here: https://developer.worldweatheronline.com/api/docs/historical-weather-api.aspx
