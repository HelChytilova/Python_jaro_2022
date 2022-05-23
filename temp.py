import pandas as pd
df=pd.read_csv("temperature.csv")
print(df[df['City']=='Prague'])
print(df[(df['AvgTemperature']>60)&(df['Region']=='Europe')])
df=df[(df['AvgTemperature']>80)|(df['AvgTemperature']<-20)]
print(df.sort_values(by=['AvgTemperature'],axis=0,ascending=True))