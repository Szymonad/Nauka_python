

class osoba():
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.wiek = 0
    def wpisz(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypisz(self):
        print(f"imie: {self.imie}")
        print(f"nazwisko: {self.nazwisko}")
        print(f"wiek: {self.wiek}")
    def zwroc(self):
        return self.imie, self.nazwisko, self.wiek





class pracownik(osoba):
    def __init__(self, wynagrodzenie = 0, staz = 0):
        super(osoba, self).__init__()
        self.wynagrodzenie = wynagrodzenie
        self.staz = staz
    def wpisz(self):
        imie = input("wpisz imie:")
        nazwisko = input("wpisz nazwisko:")
        wiek = input("wpisz wiek:")
        wynagrodzenie = input("wpisz wynagrodzenie:")
        staz = input("wpisz staz:")
        super().wpisz(imie, nazwisko, wiek)
        self.wynagrodzenie = wynagrodzenie
        self.staz = staz

    def wypisz(self):
        super().wypisz()
        print(f"wyngrodzenie: {self.wynagrodzenie}")
        print(f"staz: {self.staz}")
    def zwroc(self):
        return (*super().zwroc(), self.wynagrodzenie, self.staz) #bez gwiazdki zwraca inny rodzaj tablicy



class baza_pracownikow(pracownik):
    def __init__(self):
        self.baza = []

    def dodaj_pracownika(self):
        super().wpisz()
        #super().wypisz()
        #self.baza.append(super().zwroc())
    def wypisz_baze(self):
        print(f"baza: {self.baza}")
    def dodaj_istniejacego_pracownika(self, pracownik):
        self.baza.append(pracownik)



pracownik1 = pracownik()
baza1 = baza_pracownikow()
pracownik1.wpisz()


baza1.dodaj_pracownika()
baza1.dodaj_pracownika()

baza1.dodaj_istniejacego_pracownika(pracownik1.zwroc())
baza1.wypisz_baze()