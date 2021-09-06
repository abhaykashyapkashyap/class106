import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    icecream=[]
    colddrink=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            icecream.append(float(row["Temperature"]))
            colddrink.append(float(row["ic"]))
    return {"x":icecream,"y":colddrink}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between icecream and temperature:",correlation[0,1])
def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()