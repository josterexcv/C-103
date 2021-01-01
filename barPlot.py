import pandas as pd

import plotly.express as px

df = pd.read_csv("data.csv")
fig = x.bar(df, x = 'country', y = 'InternetUsers')
fig.show()