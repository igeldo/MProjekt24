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

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getBirthdate(self):
        return self._birthdate

    def getPhoneNumber(self):
        return self._phoneNumber

    def getAbbreviation(self):
        return self._abbreviation

    def getAge(self):
        return self.calculate_age()

    def getAll(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation]