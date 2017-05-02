import csv
import pandas as pd
import requests
import numpy as np
import os

DATA_PATH = "./Data/"
FILENAME= "raw_time_20.csv"
KEYFILE = "weatherAPI.key"

#WEATHER API INFOS: https://developer.worldweatheronline.com/api/docs/historical-weather-api.aspx
API_URL="http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
API_KEY = ""
API_FORMAT = "json"

API_HOUR_LIST = [0,300,600,900,1200,1500,1800,2100]


def callAPI(location,date):
    params = {}
    params['key']=API_KEY
    params['format']=API_FORMAT
    params['date']=date
    params['q']=location #q parameter is for location see API description
    r = requests.get(API_URL, params=params)
    return r.json()

            
with open(DATA_PATH+KEYFILE) as f:
    #read API key from file to not post it on github --> create weatherAPI.key file in data folder to use it
    API_KEY = f.read()
    print(API_KEY)
            
with open(DATA_PATH+FILENAME, newline='') as file:
    data = pd.read_csv(file)
    for index, row in data.iterrows():
        origin = row["ORIGIN_CITY_NAME"]
        date = row["FL_DATE"]
        time = row["CRS_DEP_TIME"]
        closest_time = min(API_HOUR_LIST, key=lambda x:abs(x-time)) #gets the closest time for weather forecast
        index_closest_time = API_HOUR_LIST.index(closest_time)

        json_res = callAPI(origin, date)
        
        #Filter result by closest time
        filtered_result = json_res['data']['weather'][0]['hourly'][index_closest_time]
        
        #Extract importand information out of filterd result and add to dataset
        tempC = filtered_result['tempC']
        data.set_value(index,'TEMPC',tempC)
        
        humidity = filtered_result['humidity']
        data.set_value(index,'HUMIDITY',humidity)

        windspeedKmph = filtered_result['windspeedKmph']
        data.set_value(index,'WINDSPEEDKMH',windspeedKmph)
        
        winddirDegree = filtered_result['winddirDegree']
        data.set_value(index,'WINDDIRDEGREE',winddirDegree)
        
        weatherCode = filtered_result['weatherCode'] #code-lookup: http://www.worldweatheronline.com/feed/wwoConditionCodes.txt
        data.set_value(index,'WEATHERCODE',weatherCode)
        
        visibility = filtered_result['visibility']
        data.set_value(index,'VISIBILITY',visibility)
        
        cloudcover = filtered_result['cloudcover']
        data.set_value(index,'CLOUDCOVER',cloudcover)
        
        pressure = filtered_result['pressure']
        data.set_value(index,'PRESSURE',pressure)
        
    #WRITE MODIFIED DATA TO FILE
    data.to_csv(DATA_PATH+"raw_with_weather.csv",encoding='utf-8')

        

