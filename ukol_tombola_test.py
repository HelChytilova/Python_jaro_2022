tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

listek=input("Jake mas cislo listku?")
listek=int(listek)
if listek in tombola:
      print(f"Vyhral jsi {tombola[listek]}")
      tombola.pop(listek)
else: 
      print("Nic jsi nevyhral")

print(tombola)