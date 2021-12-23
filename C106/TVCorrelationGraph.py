import plotly_express as px
import csv

with open("SizeTVHours.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x="Size of TV",y="Average time spent watching TV in a week (hours)")
    fig.show()