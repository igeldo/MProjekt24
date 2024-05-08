import datetime
from abc import abstractmethod, ABC

from datetime import date


class Person:
    def __init__(self, name, surname, birthdate, abbreviation):
        self._name = name
        self._surname = surname
        self._birthdate = birthdate
        self._abbreviation = abbreviation

    def calculate_age(self):
        today = date.today()
        birthdate = date.fromisoformat(self._birthdate)
        age = today.year - birthdate.year

        # Überprüfen, ob der Geburtstag in diesem Jahr noch nicht stattgefunden hat
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        return age

    def show_attributes(self):
        print('Vorname:', self._name)
        print('Nachname:', self._surname)
        print('Geburtsdatum:', self._birthdate)
        print('Kürzel:', self._abbreviation)
        print('Alter:', self.calculate_age())

    def create_Person(self):
        # Hier können Sie den Code einfügen, um eine neue Person anzulegen
        pass

    def delete_Person(self):
        # Hier können Sie den Code einfügen, um eine Person zu löschen
        pass

    def change_PersonDetails(self):
        # Hier können Sie den Code einfügen, um eine Person zu bearbeiten
        pass
