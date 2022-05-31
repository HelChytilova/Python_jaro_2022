import pandas as pd
df_lib=pd.read_csv("zam_liberec.csv")
df_lib['mesto']='Liberec'


df_plz=pd.read_csv("zam_plzen.csv")
df_plz['mesto']='Plzeň'


df_prh=pd.read_csv("zam_praha.csv")
df_prh['mesto']='Praha'

df_plat=pd.read_csv("platy_2021_02.csv")

df_all=pd.concat([df_lib,df_plz,df_prh],ignore_index=True)

df_all=pd.merge(df_all,df_plat, how='inner', on=['cislo_zamestnance'])

prum_plat=df_all.groupby('mesto')[['plat']].mean()
print(prum_plat)