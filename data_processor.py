import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df0_path = "/Users/keerthankg/Quantium VI/QUANTIUM-STARTER-REPO/quantium-starter-repo-main/data/daily_sales_data_0.csv"
df1_path = "/Users/keerthankg/Quantium VI/QUANTIUM-STARTER-REPO/quantium-starter-repo-main/data/daily_sales_data_1.csv"
df2_path = "/Users/keerthankg/Quantium VI/QUANTIUM-STARTER-REPO/quantium-starter-repo-main/data/daily_sales_data_2.csv"

df0 = pd.read_csv(df0_path)
df1 = pd.read_csv(df1_path)
df2 = pd.read_csv(df2_path)

df = pd.concat([df0, df1, df2], ignore_index=True)

df['price'] = df['price'].str[1:]

df['price'] = pd.to_numeric(df['price'])

df['Sales'] = df['price']*df['quantity']

df = df.drop(df[df['product'] != 'pink morsel'].index).reset_index(drop=True)

df = df.drop(columns=['product', 'price', 'quantity'])

df = df.rename(columns={"date": "Date", "region": "Region"})

# print(df)
df = df.sort_values(by="Date")

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales")

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Line Graph of Pink Morsel Sales'),

    html.Div(children='''
        A line graph portraying the sales of pink morsels according to time
    '''),

    dcc.Graph(
        id='Line Graph of Pink Morsel Sales',
        figure=fig
    )
])

app.run(debug=True)