import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    Temperature = []
    IceCreamSales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            #To remove the upper row where temp, ice cream sales and cold drink sales is written
            Temperature.append(float(row["Temperature"]))
            IceCreamSales.append(float(row["Ice-cream Sales( ₹ )"]))
    
    return{"x":Temperature,"y":IceCreamSales}

def findCorrelation(data_source):
    Correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("Correlation between temperature vs ice cream sales is ", Correlation[0,1])

def setUp():
    data_path = "IceCreamTemp.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setUp()