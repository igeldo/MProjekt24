from abc import abstractmethod, ABC



class Person:
    def __init__(self, a, b, geburtsdatum, alter, kuerzel):
        self._name = a
        self._surname = b
        self.birthdate = geburtsdatum
        self.age = alter
        self.abbreviation = kuerzel

        self._width = a
        self._length = b

    def neu_anlegen(self):
        # Hier können Sie den Code einfügen, um eine neue Person anzulegen
        pass

    def loeschen(self):
        # Hier können Sie den Code einfügen, um eine Person zu löschen
        pass

    def bearbeiten(self):
        # Hier können Sie den Code einfügen, um eine Person zu bearbeiten
        pass