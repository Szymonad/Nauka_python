class Example:
    # Metoda działająca zarówno na poziomie klasy, jak i instancji
    def describe(self=None):
        # Jeśli self jest instancją klasy Example, zwróci opis instancji
        if self:
            return f"Jestem instancją z atrybutem id {id(self)}."
        else:
            return "Jestem klasą Example."

# Wywołanie metody na poziomie instancji
inst = Example()
print(inst.describe())  # Jestem instancją z atrybutem id [unikalny_id_instancji].

# Wywołanie metody na poziomie klasy
print(Example.describe())  # Jestem klasą Example.
