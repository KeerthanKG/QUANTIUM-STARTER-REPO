import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Input, Output

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

################################################################################

colors = {
    'background': '#201F31',
    'text': '#8B1DFA'
}

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app = Dash()

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Line Graph of Pink Morsel Sales',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ), 

    html.Div(children='''
        A line graph portraying the sales of pink morsels according to time
    ''', 
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',  # Default selection
        inline=True,  # Display options inline
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='Line Graph of Pink Morsel Sales',
        figure=fig,
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
])

@app.callback(
    Output('Line Graph of Pink Morsel Sales', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.line(filtered_df, x="Date", y="Sales", title=f"Pink Morsel Sales ({selected_region.capitalize()})")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig

app.run(debug=True)