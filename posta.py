import re
with open('posta.html', encoding='utf-8') as vstup:
     posta=vstup.read()
     
posta=posta.replace('\n','\s')
seznam=re.sub('[\s\n\t]+',' ',posta)
seznam_comp=re.compile('\d{3}\s\d{2}\s[a-žA-Ž\s\d]{1,}')
vypis_seznam=seznam_comp.findall(seznam)
print(vypis_seznam)
