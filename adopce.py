import pandas as pd
df = pd.read_csv('adopce_zvirat.csv', sep=';', encoding='utf-8')
# print(df.shape)
animal=df.iloc[[34],[1,2]]
print(animal)
