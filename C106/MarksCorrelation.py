import plotly_express as px
import numpy as np
import csv

def getDataSource(data_path):
    Marks = []
    Attendance = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Attendance.append(float(row["Days Present"]))
            
    return{"x":Marks,"y":Attendance}

def findCorrelation(data_source):
    Correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("Correlation between the marks and attendance of a student is ",Correlation[0,1])

def setUp():
    data_path = "MarksAttendance.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setUp()