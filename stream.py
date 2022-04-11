class Polozka:
    def __init__(self,nazev,zanr):
        self.nazev=nazev
        self.zanr=zanr
    def __str__(self):
        return f"Nazev:{self.nazev}, zanr:{self.zanr}"

class Film(Polozka):
     def __init__(self,nazev,zanr, delka):
         super().__init__(nazev,zanr)
         self.delka=delka
     def __str__(self):
         text = super().__str__()
         text= text+f",delka:{self.delka}min"
         return text
     def get_celkova_delka(self):
         delka_tot=self.delka
         return delka_tot

class Serial(Polozka):
      def __init__(self,nazev,zanr, pocet_epizod,delka_epizody):
          super().__init__(nazev,zanr)
          self.pocet_epizod=pocet_epizod
          self.delka_epizody=delka_epizody
      def __str__(self):
         text = super().__str__()
         text= text+f",pocet_epizod:{self.pocet_epizod}, minuty:{self.delka_epizody}min"
         return text
      def get_celkova_delka(self):
         delka_tot=self.delka_epizody*self.pocet_epizod
         return delka_tot

class Uzivatel:
     def __init__(self, uzivatelske_jmeno):
         self.uzivatelske_jmeno=uzivatelske_jmeno
         self.polozky_tot=[]

     def pridej_film(self,film, delka_tot):
         self.polozky_tot.append([film, delka_tot])
     
     def vypis_polozky(self):
         self.polozky=[f[0] for f in self.polozky_tot]
             
     def delka_zhlednuti(self):
         self.delka=sum(film[1] for film in self.polozky_tot)
     
     def __str__(self):
         
         return f"Uzivatel {self.uzivatelske_jmeno} zhlednul nasledujici polozky {self.polozky} o celkove delce:{self.delka} min"
    
        

film=Film('Forrest Gump','Komedie/Drama',142)
serial=Serial('The IT Crowd','Komedie',24,26)
Users={}
Users["U1"]=Uzivatel('Sojka')
Users["U2"]=Uzivatel('Straka')
def sledovani (uzivatel, polozka):
    if polozka==film:
       uzivatel.pridej_film(polozka.nazev,Film.get_celkova_delka(polozka))
       uzivatel.vypis_polozky()
       uzivatel.delka_zhlednuti()
    else:
        uzivatel.pridej_film(polozka.nazev,Serial.get_celkova_delka(polozka))
        uzivatel.vypis_polozky()
        uzivatel.delka_zhlednuti()
        
    return(print(uzivatel))
    
sledovani(Users["U1"],film)
sledovani(Users["U1"],serial)
sledovani(Users["U2"],serial)
sledovani(Users["U2"],film)