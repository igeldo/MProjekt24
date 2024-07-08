from datetime import date


class Person:
    # nimmt mehrere Parameter entgegen, die zur Initialisierung des Objekts verwendet werden.
    def __init__(self, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str):
        self._name = name # Hier wird die Instanzvariable _name mit dem übergebenen name Wert initialisiert.
        self._surname = surname
        self._birthdate = birthdate
        self._phoneNumber = phoneNumber
        self._abbreviation = abbreviation

    def calculate_age(self):
        today = date.today()
        birthdate = date.fromisoformat(self._birthdate)
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

    def get_name(self):
        return self._name # Diese Methode gibt den Wert der Instanzvariable _name des Patienten-Objekts zurück.

    def get_surname(self):
        return self._surname

    def get_birthdate(self):
        return self._birthdate

    def get_phone_number(self):
        return self._phoneNumber

    def get_abbreviation(self):
        return self._abbreviation

    def get_age(self):
        return self.calculate_age()

    def get_all(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation]
    # Diese Methode gibt eine Liste mit allen Basiseigenschaften des Patienten-Objekts zurück,
    # einschließlich Name, Nachname, Geburtsdatum, Telefonnummer und Abkürzung.
