import pandas as pd
import plotly.express as px

data = pd.read_csv("C:/Users/C/OneDrive/Desktop/Coding/python/Charts and Data/Copy+of+data+-+data.csv")
figure = px.scatter(data, x="date", y="cases", color="country", title="NUmber of COVID19 Cases per Country")

figure.show()