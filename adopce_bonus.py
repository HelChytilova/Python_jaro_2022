import pandas as pd
df = pd.read_csv('adopce_zvirat.csv', sep=';', index_col='nazev_cz', encoding='utf-8')
# print(df.index.is_unique)
# print(df.columns)
df=df.sort_index()
print(df)
print(df.loc[['Outloň váhavý']])
print(df.loc['Želva Smithova':'Želva žlutočelá'])