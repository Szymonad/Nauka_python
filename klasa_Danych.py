from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    email: str

# Przykładowe użycie
person = Person(first_name="Anna", last_name="Kowalska", age=30, email="anna.kowalska@o2.com")
person2 = Person(first_name="Adam", last_name="Małysa", age=40, email="a.mal@o2.com")
person3 = Person(first_name="Adam", last_name="Małysa", age=40, email="a.mal@o2.com")
# Wyświetlenie obiektu
print(person)
print(person2)

print(person3 == person2)
# Dostęp do atrybutów
print(f"Imię: {person.first_name}, Nazwisko: {person.last_name}, Wiek: {person.age}, Email: {person.email}")





########################################## inny dłuższy sposób#########################333
# class Person:
#     def __init__(self, first_name, last_name, age, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#
#     def __repr__(self):  # klasa reprezentacyjna tekstowa
#         return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', age={self.age}, email='{self.email}')"
#
#     def __eq__(self, other): #klasa porównawcza, umożliwia porównywanie 2 różnych instacji
#         if isinstance(other, Person):
#             return (self.first_name == other.first_name and
#                     self.last_name == other.last_name and
#                     self.age == other.age and
#                     self.email == other.email)
#         return False
#
#
# # Przykładowe użycie
# person = Person(first_name="Anna", last_name="Kowalska", age=30, email="anna.kowalska@o2.com")
#
# # Wyświetlenie obiektu
# print(person)
#
# # Dostęp do atrybutów
# print(f"Imię: {person.first_name}, Nazwisko: {person.last_name}, Wiek: {person.age}, Email: {person.email}")
