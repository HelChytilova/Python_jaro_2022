
from datetime import date, time, datetime

start_date1=datetime(2021,7,1)
end_date1=datetime(2021,8,10)
start_date2=datetime(2021,8,11)
end_date2=datetime(2021,8,31)


visit=input('Zadej datum ')
visit=datetime.strptime(visit, "%d.%m.%Y")
if visit<start_date1 or visit>end_date2:
    print('Letni kino je v teto dobe uzavrene')
else:
    tickets=input('Zadej pocet vstupenek ')
    tickets=int(tickets)
    if visit>=start_date1 and visit<=end_date1:
        print(f'Finalni cena je {250*tickets} Kc')
    else:
        print(f'Finalni cena je {180*tickets} Kc')



