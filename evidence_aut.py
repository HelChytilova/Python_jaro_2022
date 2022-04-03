class Auto:
    def __init__(self,SPZ,znacka_typ,najeto_km):
        self.SPZ=SPZ
        self.znacka_typ=znacka_typ
        self.najeto_km=najeto_km
        self.volne=True

    def pujc_auto(self):
         if self.volne==True:
            self.volne=False
            print('Potvrzuji zapůjčení vozidla')
         else:
             print('Vozidlo není momentálně volné')
    
    def get_info(self):
        return print( f"{self.SPZ} + {self.znacka_typ}")


pujcovna={}
pujcovna['Peugeot']=Auto('4A2 3020','Peugeot 403 Cabrio',47534)
pujcovna['Skoda']=Auto('1P3 4747','Škoda Octavia',41253)

def pujceni_auta(auto):
   info=pujcovna[auto].get_info()
   pujceni= pujcovna[auto].pujc_auto()
   return info
   return pujceni

while True:
    try: 
       auto = input('Jake chces auto? Muzes si pujcit jen Skoda nebo Peugeot ')
       assert auto  in ['Skoda','Peugeot']
     
    except AssertionError:
           print("Mame pouze auto Skoda nebo Peugeot!")
    else:
           break

pujceni_auta(auto)


auto = input('Jake chces auto? Muzes si pujcit jen Skoda nebo Peugeot ')
if auto in pujcovna:
      pujceni_auta(auto)
else:
    print('Mame pouze auto Skoda nebo Peugeot!')







    
