


import math
from xmlrpc.client import boolean



def over_numb(numb:str):
  numb=numb.replace(" ","")
  result=boolean
  if ('+420' in numb and len(numb)==13) or len(numb)==9:
      result=True
  else:
      result=False
  return result  


def cena_sms(text:str):
    price=float
    price=math.ceil(len(text)/180)*3
    return price

numb=input("Zadej cislo ")
if over_numb(numb)==True:
    text=input('Zadej text ')
    cena=cena_sms(text)
    print(f"cena sms je {cena} Kc")
else:
    print('Spatny format cisla')

    


    




        
 
