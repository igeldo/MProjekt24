import datetime
from abc import abstractmethod, ABC


class Person:
    def __init__(self, a, b, c, d):
        self._name = a
        self._surname = b
        self._birthdate = datetime.date(2018, 5, 12)
        self._abbreviation = d

    def show_attributes(self):
        print('Vorname: ' + self._name)
        print('Nachname: ' + self._surname)
        print('Geburtsdatum: ' + )
        print('Kürzel: ' + self._abbreviation)


    def neu_anlegen(self):
        # Hier können Sie den Code einfügen, um eine neue Person anzulegen
        pass

    def loeschen(self):
        # Hier können Sie den Code einfügen, um eine Person zu löschen
        pass

    def bearbeiten(self):
        # Hier können Sie den Code einfügen, um eine Person zu bearbeiten
        pass
