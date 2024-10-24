####################KONSTRUKTOR, INICJALIZACJA REPREZENTACJA##########################

# __init__(self, ...) – Konstruktor klasy, wywoływany przy tworzeniu nowego obiektu. Służy do przypisywania wartości atrybutom obiektu.
#
# __new__(cls, ...) – Metoda odpowiedzialna za tworzenie nowego obiektu klasy. Rzadko używana w porównaniu do __init__.
#
# __del__(self) – Destruktor, wywoływany przy usuwaniu obiektu. Używany, gdy chcemy wykonać specjalne operacje podczas zwalniania zasobów, np. zamknięcie plików.
#
# __repr__(self) – Reprezentacja tekstowa obiektu, używana do debugowania. Zwraca czytelną formę klasy, np. Person(name='John').
#
# __str__(self) – Używana przez funkcję print() do wyświetlania obiektu. Może różnić się od __repr__.
#


####################OPERACJE MATEMATYCZNE##########################
# przykład
def __add__(self, other): # – Obsługa operatora + dla odejmowania.
    return self.value + other.value


# __sub__(self, other) – Obsługa operatora - dla odejmowania.
#
# __mul__(self, other) – Obsługa operatora * dla mnożenia.
#
# __truediv__(self, other) – Obsługa operatora / dla dzielenia.
#
# __mod__(self, other) – Obsługa operatora % dla operacji modulo.
#
# __pow__(self, other) – Obsługa operatora ** dla potęgowania.




####################PORÓWNANIE OBIEKTÓW##########################
#przykład
def __eq__(self, other): # Porównywanie ==. Określa, kiedy dwa obiekty są równe.
    return self.name == other.name

#
# __ne__(self, other) – Porównywanie !=. Określa, kiedy dwa obiekty nie są równe.
#
# __lt__(self, other) – Porównywanie < (mniej niż).
#
# __le__(self, other) – Porównywanie <= (mniej lub równe).
#
# __gt__(self, other) – Porównywanie > (więcej niż).
#
# __ge__(self, other) – Porównywanie >= (więcej lub równe).


################################INNE#######################################

def __iter__(self):
    return iter(self.data)
