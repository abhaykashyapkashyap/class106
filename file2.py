import csv
import plotly.express as px
with open("cups of coffee vs hours of sleep.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Coffee",y="sleep")
    fig.show()