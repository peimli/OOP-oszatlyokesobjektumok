'''
#1.2 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra
is egy-egy metódussal!


class Negyzet:
    def __init__(self,oldal):
        self.oldal = oldal
        
    def terulet(self):
        return pow(self.oldal, 2)
    def kerulet(self):
        return self.oldal * 4


a = Negyzet(int(input('Adja meg a négyzet oldalának hosszát!')))
print(a.terulet())
print(a.kerulet())


#1.3 Feladat
Az 1.1 feladatban meghatározottak szerint készíts egy programot,
amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg,
amíg a felhasználó 0 értéket nem ad meg! Ezen adat alapján a program hozzon létre negyzet
objektumokat, melyeket egy listában tárol! A program írja ki a megadott négyzetek
oldalhosszát, kerületét és területét!

l = []
beker = ''
while beker != 0:
    beker = int(input('Adja meg a négyzet oldal hosszát!'))
    l.append(str(beker))
l.remove(l[-1])


for sor in l:
    c = Negyzet(int(sor))
    print(f'A {sor} terulete: {c.terulet()}, kerülete: {c.kerulet()}')

#2. Feladat
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait
(név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen
határozza meg a program! Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
'''

import random
class Kutya:        
    def neve(self):
        a = input('Adja meg a kutya nevét!')
        return a
    def kora(self):
        a = random.randint(1,23)
        return a
    def neme(self):
        b = random.randint(1,2)
        if b == 1:
            return 'lány'
        if b == 2:
            return 'fiú'

kutya = Kutya()
nev1 = kutya.neve()
kora1 = kutya.kora()
neme1 = kutya.neme()
print(f'A kutya neve: {nev1}, életkora: {kora1}, neme: {neme1}.')

