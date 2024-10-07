class Animal:
    # Atrybut klasowy
    species = "Animalllll"

    # Metoda instancyjna
    def __init__(self, name, age):
        self.name = name  # Atrybut instancyjny
        self.age = age    # Atrybut instancyjny

    def speak(self):
        """Metoda instancyjna, która działa na instancji."""
        return f"{self.name} makes a noise."

    # Metoda klasowa
    @classmethod
    def describe_species(cls):
        """Metoda klasowa, która działa na klasie."""
        return f"All animals belong to the {cls.species} kingdom."

    # Metoda statyczna
    @staticmethod
    def is_adult(age):
        """Metoda statyczna, która nie potrzebuje dostępu ani do klasy, ani do instancji."""
        return age >= 2

    # Metoda specjalna (magic method)
    def __str__(self):
        """Metoda specjalna zwracająca opis obiektu."""
        return f"{self.name} is {self.age} years old."


# Dziedziczenie
class Dog(Animal):
    def speak(self):
        """Przeciążenie metody instancyjnej."""
        return f"{self.name} barks."


# Tworzenie instancji klasy Dog
rex = Dog("Rex", 5)

# Użycie metody instancyjnej
print(rex.speak())  # Rex barks.

# Użycie metody klasowej
print(Dog.describe_species())  # All animals belong to the Animallll kingdom.

# Użycie metody statycznej
print(Dog.is_adult(5))  # True

# Użycie metody specjalnej (print automatycznie używa __str__)
print(rex)  # Rex is 5 years old.
