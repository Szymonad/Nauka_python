class SingletonMeta(type):
    """Metaklasa, która zapewnia, że istnieje tylko jedna instancja klasy."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Kalkulator(metaclass=SingletonMeta):
    def __init__(self, liczba1=0, liczba2=0):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

    def suma(self):
        wynik = self.liczba1 + self.liczba2
        print(f"Suma = {wynik}")

    def mnozenie(self):
        wynik = self.liczba1 * self.liczba2
        print(f"Wynik mnożenia = {wynik}")

    def dzielenie(self):
        if self.liczba2 == 0:
            print("Nie dziel przez 0!")
        else:
            wynik = self.liczba1 / self.liczba2
            print(f"Wynik dzielenia = {wynik}")
    def wpisz_liczby(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

class Historia(Kalkulator):
    #def __init__(self, liczba1=0, liczba2=0):
    def __init__(self):
        #super().__init__(liczba1, liczba2)
        #super(Historia, self).__init__()
        self.lista_liczba1 = []  # Lista przechowująca historię pierwszej liczby
        self.lista_liczba2 = []  # Lista przechowująca historię drugiej liczby


    def wypisz_historie(self):
        print(f"Historia liczba1: {self.lista_liczba1}")
        print(f"Historia liczba2: {self.lista_liczba2}")

    def aktualizuj(self):
        self.lista_liczba1.append(self.liczba1)
        self.lista_liczba2.append(self.liczba2)


# Pętla do wykonywania działań
his = Historia()
his2 = Historia()

while True:

    opcja = input("Naciśnij 'q', aby zakończyć program, lub Enter, aby kontynuować: ").lower()

    if opcja == 'q':
        print("Zakończono program.")
        break  # Zakończenie pętli, jeśli użytkownik wpisze 'q'

    try:
        # Wprowadzenie dwóch liczb od użytkownika
        aa = int(input("Podaj pierwszą liczbę: "))
        bb = int(input("Podaj drugą liczbę: "))


        his.wpisz_liczby(aa, bb)
        his.suma()
        his.mnozenie()
        his.dzielenie()
        his2.aktualizuj()
        his.wypisz_historie()


    except ValueError:
        print("podaj int!")




        #######utworzenie nowego brancha##########