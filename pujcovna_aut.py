
soubor=input('zadej nazev souboru ')
with open(soubor+'.txt', encoding='utf-8') as vstup:
    seznam = vstup.readlines()

radky = [auto.strip() for auto in seznam]

total_km=sum(float(auto[9:13].replace(',','.'))for auto in radky)
print(total_km)

