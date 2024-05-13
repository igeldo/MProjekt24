from datetime import date


class Person:
    def __init__(self, name: str, surname: str, birthdate, phoneNumber: int, abbreviation: str):
        self._name = name
        self._surname = surname
        self._birthdate = birthdate
        self._phoneNumber = phoneNumber
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
        print('Telefon: ', self._phoneNumber)
        print('Kürzel:', self._abbreviation)
        print('Alter:', self.calculate_age())
