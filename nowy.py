# def znajdz_nwd(x, y):
#     while y:
#         print(x)
#         print(y)
#         x, y = y, x % y
#     return x
#
# # Wprowadzenie danych od użytkownika
# liczba1 = 70
# liczba2 = 15
#
# # Obliczanie NWD
# nwd = znajdz_nwd(liczba1, liczba2)
#
# # Wyświetlenie wyniku
# print(f"NWD liczb {liczba1} i {liczba2} to: {nwd}")





# def count_pairs(arr):
#     n = len(arr)
#     count = 0
#     number = 0
#     # Przechodzimy przez wszystkie możliwe pary (i, j)
#     for i in range(n):
#         for j in range(i + 1, n):
#             number = number + 1
#             print(f"i = {i}")
#             print(f"j = {j}")
#
#             print(f"arr[i] = {arr[i]}")
#             print(f"arr[j] = {arr[j]}")
#             # Sprawdzamy warunek z treści zadania
#             if (arr[i] ^ arr[j]) > (arr[i] & arr[j]):
#                 count += 1
#     return count, number
#
# # Przykład użycia
# arr = [6,8,7,4,2,5]
# result, num = count_pairs(arr)
# print(f"Liczba par spełniających warunek: {result}")
# print(f"ilość przejść: {num}")

# def min_moves(word):
#     moves = 0
#     n = len(word)
#
#     # Użycie stosu do przechowywania znaków
#     stack = []
#
#     i = 0
#     while i < n:
#         # Jeśli stos jest pusty lub znak nie ma pary, dodajemy go do stosu
#         if not stack or stack[-1] != word[i]:
#             if stack:  # Sprawdzamy, czy stos nie jest pusty przed wydrukowaniem
#                 print(f"Top stosu: {stack[-1]}")
#             stack.append(word[i])
#         else:
#             # Jeśli znak ma parę, usuwamy go ze stosu
#             stack.pop()
#             moves += 1
#         i += 1
#         print(f"Stos po iteracji {i}: {stack}")
#
#     return moves
#
#
#
# # Testowanie z przykładem
# word = "baabacaa"
# result = min_moves(word)
# print(f"Minimalna liczba ruchów dla słowa '{word}' to: {result}")

# def count_divisible_triplets(arr, d):
#     n = len(arr)
#     count = 0
#
#     # Sprawdzamy wszystkie możliwe trójki (i, j, k) gdzie i < j < k
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 # Obliczamy sumę trójki
#                 triplet_sum = arr[i] + arr[j] + arr[k]
#                 # Sprawdzamy, czy suma jest podzielna przez d
#                 if triplet_sum % d == 0:
#                     count += 1
#     return count
#
#
# # Przykład użycia
# arr = [3, 3, 4, 7, 8]
# d = 5
# result = count_divisible_triplets(arr, d)
# print(f"Liczba trójek, których suma jest podzielna przez {d}, to: {result}")


# def fizzBuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
# # Przykład użycia:
# n = 15
# fizzBuzz(n)

#
# def odd_even_transform(arr, n):
#     for _ in range(n):
#         for i in range(len(arr)):
#             if arr[i] % 2 == 0:  # Parzysta
#                 arr[i] -= 3
#             else:                # Nieparzysta
#                 arr[i] += 3
#     return arr
#
# # Przykład użycia
# arr = [3, 4, 9]
# n = 3
# result = odd_even_transform(arr, n)
# print(f"Po {n} transformacjach, tablica to: {result}")
def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    products = list(zip(unitsPerBox, boxes))


    products.sort(reverse=True, key=lambda x: x[0])
    print(products)
    total_units = 0

    for units, count in products:
        if truckSize <= 0:
            break
        boxes_to_take = min(count, truckSize)
        print(f"boxes to take: {boxes_to_take}")
        total_units += boxes_to_take * units
        print(f"total units: {total_units}")
        truckSize -= boxes_to_take

    return total_units

print(getMaxUnits([100, 7 , 10], [3, 15, 100], 15))

