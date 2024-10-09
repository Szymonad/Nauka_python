import math
import numpy as np


macierz_A = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-2, -1, 0, 1, 2],
])
macierz_B = np.array([
    [1, 3, 5, 7, 9],
    [0.5, 1, 1.5, 2, 2.5],
])

macierz_C = np.random.uniform(0, 2, (4, 5))

wektor_A1 = macierz_A[1, :]

macierz_A2 = macierz_A[:, 1:5]

macierz_A3 = macierz_A[1:3, 2:5]

macierz_A4 = macierz_A[:, [0, 2, 4]]


print(f"wektor A1: {wektor_A1}")
print(f"macierz A2: {macierz_A2}")
print(f"macierz A3: {macierz_A3}")
print(f"macierz A4: {macierz_A4}")

#####################RÓWNANIA####################


y = 4
z = 7
x = 3


def rownanie_1(y, z, x):
    return math.sqrt(z) * z ** 4 * x * y * 2.8 ** y / (math.exp(y) * (y + z * math.sqrt(y)))


def rownanie_2(y, z, x):
    return math.log10(y) * (-3) * z ** y / (10 ** x * math.cos(y))


def rownanie_3(y, z, x):
    return z * y * z * math.log(x)



wynik_1 = rownanie_1(y, z, x)
wynik_2 = rownanie_2(y, z, x)
wynik_3 = rownanie_3(y, z, x)

print(f"wynik_1: {wynik_1}")
print(f"wynik_2: {wynik_2}")
print(f"wynik_3: {wynik_3}")

wynik_1 = round(wynik_1, 3)
wynik_2 = round(wynik_2, 3)
wynik_3 = round(wynik_3, 3)

print(f"wynik_1: {wynik_1}")
print(f"wynik_2: {wynik_2}")
print(f"wynik_3: {wynik_3}")

wektor_wyniki = np.array([[wynik_1],
                          [wynik_2],
                          [wynik_3]])

print(f"wektor wyników: {wektor_wyniki}")

wektor_wyniki_transponowany = wektor_wyniki.T

print(f"wektor wyników transponowany: {wektor_wyniki_transponowany}")

SumW = np.sum(wektor_wyniki_transponowany)

print(f"suma wyników: {SumW}")

print(type(SumW))