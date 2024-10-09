import numpy as np

# A = [1, 2, 3, 4]
# print(A[1])
#
#
# for a in np.arange (1,5, 0.1):
#     print(f"{a:.3f}", f"{a:.6f}")

#
# class Configuration:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
#             cls._instance.settings = {}  # Tworzymy pole settings przy pierwszej instancji
#         return cls._instance
#
#     def set_setting(self, key, value):
#         self.settings[key] = value
#
#     def get_setting(self, key):
#         return self.settings.get(key, None)


# import os
#
# # Przykładowa lista katalogów
# dirs = ["katalog_1", "katalog_2", "katalog_3"]
#
# # Lista plików w katalogach (załóżmy, że mamy po 3, 5 i 2 pliki)
# mock_files = {
#     "katalog_1": ["plik1", "plik2", "plik3"],
#     "katalog_2": ["plik1", "plik2", "plik3", "plik4", "plik5"],
#     "katalog_3": ["plik1", "plik2"]
# }
#
# # Funkcja, która "symuluje" os.listdir, aby ten kod działał bez rzeczywistych katalogów
# def mock_listdir(directory):
#     return mock_files.get(directory, [])
#
# # Właściwe wyrażenie listowe
# labels = [[i] * len(mock_listdir(dir)) for i, dir in enumerate(dirs)]
#
# print(labels)

# class Vehicle:  #klasa bazowa
#     def __init__(self, brand, moc):
#         self.brand = brand
#         self.moc = moc
#
#     def drive(self):
#         print(f"{self.brand}")
#         print(self.brand)
#
#     def how_many_power(self):
#         print(f"moc = {self.moc} km.")
#
#
# class Car(Vehicle):  # Klasa pochodna
#     def __init__(self, brand, model, moc):
#         super().__init__(brand, moc)
#         self.model = model
#
#     def honk(self):
#         print(f"{self.brand} {self.model} ")
#
#
#
# pojazd = Car("Mazda", "RX-7", 200)  #
# pojazd.drive()
# pojazd.honk()
# pojazd.how_many_power()


# from abc import ABC, abstractmethod
#
# # Definicja klasy abstrakcyjnej Shape
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Zwraca pole powierzchni figury"""
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         """Zwraca obwód figury"""
#         pass
#
#     def description(self):
#         """Metoda nieabstrakcyjna - opcjonalna do nadpisania"""
#         return "This is a shape."
#
# # Konkretna klasa Circle dziedzicząca po Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# # Konkretna klasa Rectangle dziedzicząca po Shape
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def description(self):
#         return f"This is a rectangle with width {self.width} and height {self.height}."
#
#
# # Przykład użycia klas pochodnych
# shapes = [
#     Circle(5),          # Tworzymy obiekt Circle o promieniu 5
#     Rectangle(4, 6),    # Tworzymy obiekt Rectangle o szerokości 4 i wysokości 6
# ]
#
# for shape in shapes:
#     print(f"{shape.__class__.__name__} area: {shape.area()}")           # Wywołanie metody area()
#     print(f"{shape.__class__.__name__} perimeter: {shape.perimeter()}") # Wywołanie metody perimeter()
#     print(shape.description())                                          # Opcjonalne wywołanie description()
#     print()


class Kalkulator:
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
    def __init__(self, liczba1=0, liczba2=0):
        super().__init__(liczba1, liczba2)
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
        his.aktualizuj()
        his.wypisz_historie()


    except ValueError:
        print("podaj int!")

