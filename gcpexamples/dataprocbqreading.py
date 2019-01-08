import os
import sys
#import google.datalab.bigquery as bq
from google.cloud import bigquery
import pandas as pd
import numpy as np
import shutil
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from pyspark import SparkContext, SparkConf, SQLContext

conf = SparkConf().setAppName("compilingtables")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

exportyear = [2015,2016,2017,2018]

def weatheryearcleaning(year):
    
    # Get ther initial table along with the needed columns
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig()
    sourcet = 'bigquery-public-data.ghcn_d.ghcnd_{}'.format(year)
    query = """
    select closest.id, closest.name, closest.latitude, closest.longitude, element as stats_name, value as stats_value, date
    from {} as data right join (
        select id, name, state, latitude, longitude, ST_DISTANCE(ST_GEOGPOINT(longitude, latitude),ST_GEOGPOINT( -113.580001831, 53.309700012200004 )) / 1000.0 as distance
            from `bigquery-public-data.ghcn_d.ghcnd_stations`
            where
                longitude is not null and latitude is not null
       
        ) as closest on data.id = closest.id
    where
        extract(year from data.date) =  {}
       and closest.distance <= 20
       and element in ('TMAX','TMIN','TAVG','PRCP','SNOW','SNWD','WSFG','AWDR','AWND','TSUN')  
       OR element like 'WT%' OR element like 'WV%'
    order by closest.id, data.date 
    """.format(sourcet,year)

    query_job = client.query(query , job_config=job_config )
    print(type(query))
   

weatheryearcleaning(2018)
