from allatok import Allat, Hullo, Madar, Keteltu
from emlos import Emlos, Macska, Kutya

allatok = []
with open('allatok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        nev = adatok[0]
        faj = adatok[1]
        eletkor = int(adatok[2])
        szorzet_szine = adatok[3]
        allat = {'faj': faj, 'eletkor': eletkor, 'szorzet_szine': szorzet_szine}
        if faj == "kutya":
            allatok.append(Kutya(nev, faj, eletkor, szorzet_szine))
        elif faj == "macska":
            allatok.append(Macska(nev, faj, eletkor, szorzet_szine))
        elif faj == "hullo":
            allatok.append(Hullo(nev, faj, eletkor, szorzet_szine))
        elif faj == "madar":
            allatok.append(Madar(nev, faj, eletkor, szorzet_szine))
        elif faj == "keteltu":
            allatok.append(Keteltu(nev, faj, eletkor, szorzet_szine))


for i in allatok:
    print(i)
    if isinstance(i, Kutya):
        i.ugat()
    elif isinstance(i, Macska):
        i.dorombol
    elif isinstance(i, Madar):
        i.csiripel
    elif isinstance(i, Hullo):
        i.napozik
    elif isinstance(i, Keteltu):
        i.brekeg