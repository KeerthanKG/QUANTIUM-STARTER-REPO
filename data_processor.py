import pandas as pd

df0_path = "quantium-starter-repo-main/data/daily_sales_data_0.csv"
df1_path = "quantium-starter-repo-main/data/daily_sales_data_1.csv"
df2_path = "quantium-starter-repo-main/data/daily_sales_data_2.csv"

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

print(df)