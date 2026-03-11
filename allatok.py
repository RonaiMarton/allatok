class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev}, {self.faj}, {self.eletkor} eves, elohelye {self.elohely}, merete: {self.meret}"
    

class Madar(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "madar", eletkor_, elohely_, meret_)
    
    def csiripel(self):
        print(f"{self.nev} csiripel")


class Keteltu(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "keteltu", eletkor_, elohely_, meret_)

    def brekeg(self):
        print(f"{self.nev} brekeg")


class Hullo(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "hullo", eletkor_, elohely_, meret_)

    def napozik(self):
        print(f"{self.nev}, napozik a kovon")

    