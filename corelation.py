import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        graph = px.scatter(df,x="Days Present", y="Marks In Percentage")
        graph.show()

def getDataSource(data_path):
    percent = []
    days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percent.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x" : percent, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0,1])

def setup():
    data_path  ="C:/Users/HOME/Downloads/co/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
