from abc import abstractmethod, ABC



class Person:
    def __init__(self, a, b, c, d, e):
        self._name = a
        self._surname = b
        self._birthdate = c
        self._age = d
        self._abbreviation = e

    def neu_anlegen(self):
        # Hier können Sie den Code einfügen, um eine neue Person anzulegen
        pass

    def loeschen(self):
        # Hier können Sie den Code einfügen, um eine Person zu löschen
        pass

    def bearbeiten(self):
        # Hier können Sie den Code einfügen, um eine Person zu bearbeiten
        pass