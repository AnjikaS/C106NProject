import plotly_express as px
import numpy as np
import csv

def getDataSource(data_path):
    TVSize = []
    HoursWatching = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            TVSize.append(float(row["Size of TV"]))
            HoursWatching.append(float(row["Average time spent watching TV in a week (hours)"]))
            
    return{"x":TVSize,"y":HoursWatching}

def findCorrelation(data_source):
    Correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("Correlation between the size of the TV and how long a person watches it is ",Correlation[0,1])

def setUp():
    data_path = "SizeTVHours.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setUp()