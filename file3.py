import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    time=[]
    size=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            time.append(float(row["time"]))
            size.append(float(row["Size"]))
    return {"x":time,"y":size}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between time and size of tv:",correlation[0,1])
def setup():
    data_path="Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()